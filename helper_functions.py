
import torch
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
import torchvision
import torchvision.models
from tqdm.auto import tqdm
from timeit import default_timer as time
from typing import Callable

device = "cuda" if torch.cuda.is_available() else "cpu"

# STEP FUNCTIONS FOR TRAINING 
def train_step(model: torch.nn.Module,
               loss_fn: torch.nn.Module,
               data_loader: torch.utils.data.DataLoader,
               optimizer: torch.optim.Optimizer,
               accuracy_fn,
               device: torch.device):
    """Perform training on model trying to learn on data_loader"""
    model.train()
    loss = 0
    accuracy_fn.reset()

    for (X, y) in tqdm(data_loader, desc="Training Batches", leave=False):
        X, y = X.to(device), y.to(device)

        # 1. Forward pass
        outputs = model(X)
        y_preds = outputs.logits if hasattr(outputs, "logits") else outputs

        # 2. Calculate loss and update metrics
        train_loss_batch = loss_fn(y_preds, y)
        loss += train_loss_batch.item()
        accuracy_fn.update((y_preds, y))

        # 3. Backward pass and optimization steps
        optimizer.zero_grad()
        train_loss_batch.backward()
        optimizer.step()

    loss /= len(data_loader)
    accuracy = accuracy_fn.compute()

    print(f"Train loss: {loss:.4f} | train accuracy: {accuracy:.4f}")
    return (loss, accuracy)

def test_step(model: torch.nn.Module,
              loss_fn: torch.nn.Module,
              data_loader: torch.utils.data.DataLoader,
              accuracy_fn,
              device: torch.device):
    """Perform testing on model going over data_loader"""
    test_loss = 0
    accuracy_fn.reset()
    model.eval()

    with torch.inference_mode():
        for X_test, y_test in tqdm(data_loader, desc="Testing Batches", leave=False):
            X_test, y_test = X_test.to(device), y_test.to(device)

            # 1. Forward pass
            outputs = model(X_test)
            y_test_preds = outputs.logits if hasattr(outputs, "logits") else outputs

            # 2. Calculate batch loss
            test_loss_batch = loss_fn(y_test_preds, y_test)
            test_loss += test_loss_batch.item()

            # 3. Track metrics
            accuracy_fn.update((y_test_preds, y_test))

        test_loss /= len(data_loader)
        test_acc = accuracy_fn.compute()

    print(f"Test loss: {test_loss:.4f} | test accuracy: {test_acc:.4f}")
    return (test_loss, test_acc)


# PRINT TRAINING TIME
def print_train_time(start: float, end: float, device: torch.device = None):
    """Prints difference between start and end time"""
    total_time = end - start
    print(f"Train time for device {device}: {total_time:.2f} seconds")
    return total_time


# EVALUATE THE MODEL
def eval_model(
    model: torch.nn.Module,
    data_loader: torch.utils.data.DataLoader,
    loss_fn: torch.nn.Module,
    accuracy_fn,
    device: torch.device
):
    """Evaluates the given model on the target data loader."""
    model.eval()
    accuracy_fn.reset()
    
    loss = 0.0
    
    with torch.inference_mode():
        for X, y in tqdm(data_loader, desc="Evaluating"):
            X, y = X.to(device), y.to(device)
            y_preds = model(X)

            logits = y_preds.logits if hasattr(y_preds, 'logits') else y_preds

            loss_batch = loss_fn(logits, y)
            loss += loss_batch.item() # FIX: used .item() here
            accuracy_fn.update((logits, y))

        loss /= len(data_loader)
        accuracy = accuracy_fn.compute()

    if isinstance(accuracy, torch.Tensor): 
        accuracy = accuracy.item()

    return {
        "model_name": model.__class__.__name__,
        "loss": loss,
        "accuracy": accuracy
    }

# TRAIN FUNCTION
def train_give_results(model: torch.nn.Module,
                         loss_fn: torch.nn.Module,
                         optimizer: torch.optim.Optimizer,
                         accuracy_fn: Callable,
                         train_dataloader: torch.utils.data.DataLoader,
                         test_dataloader: torch.utils.data.DataLoader,
                         train_step: Callable,
                         test_step: Callable,
                         print_train_time: Callable,
                         lr_scheduler: Callable,
                         patience: int,
                         epochs: int,
                         device: torch.device):

    training_results = {
        "results": [],
        "train_time": 0,
        "model_layers": None,
        "device": device
    }

    # FIX: Changed 'timer()' to the correct imported alias 'time()'
    time_before_train = time()

    patience_counter = 0
    best_loss = float("inf")

    for epoch in tqdm(range(epochs), desc="Total Epochs"):
        print(f"\nepoch: {epoch}--------------")

        ### 1. Training Step
        train_loss, train_acc = train_step(
            model=model,
            loss_fn=loss_fn,
            optimizer=optimizer,
            accuracy_fn=accuracy_fn,
            data_loader=train_dataloader,
            device=device
        )

        ### 2. Testing Step
        test_loss, test_acc = test_step(
            model=model,
            loss_fn=loss_fn,
            data_loader=test_dataloader,
            accuracy_fn=accuracy_fn,
            device=device
        )

        if isinstance(train_acc, torch.Tensor): train_acc = train_acc.item()
        if isinstance(test_acc, torch.Tensor): test_acc = test_acc.item()

        ### 3. Apply lr scheduler
        lr_scheduler.step(test_loss)

        ### 4. Apply early stopping
        if test_loss < best_loss:
            best_loss = test_loss
            patience_counter = 0
            torch.save(model.state_dict(), "best_model.pt")
            print(f"🔥 New best model saved with test loss: {test_loss:.4f}")
        else:
            patience_counter += 1

        if patience_counter >= patience:
            print(f"🛑 Early stopping triggered at epoch {epoch}")
            break

        ### 5. SAVE RESULTS
        training_results['results'].append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_acc": train_acc,
            "test_loss": test_loss,
            "test_acc": test_acc,
        })

    time_after_train = time()
    train_time = print_train_time(time_before_train, time_after_train, device=device)

    training_results["train_time"] = train_time
    training_results["device"] = device

    if hasattr(model, "features"):
        training_results["model_layers"] = str(model.features)
    else:
        training_results["model_layers"] = str(type(model))

    return training_results

# just changed the above train_give_resultsfor CosineAnnealingWarmRestarts schedular
def train_give_results_sc(model: torch.nn.Module,
                          loss_fn: torch.nn.Module,
                          optimizer: torch.optim.Optimizer,
                          accuracy_fn: Callable,
                          train_dataloader: torch.utils.data.DataLoader,
                          test_dataloader: torch.utils.data.DataLoader,
                          train_step: Callable,
                          test_step: Callable,
                          print_train_time: Callable,
                          lr_scheduler: Callable, 
                          patience: int, 
                          epochs: int,
                          device: torch.device):

    ### INITIALIZE RESULTS DICTIONARY
    training_results = {
        "results": [],
        "train_time": 0,
        "model_layers": None,
        "device": device
    }

    # FIX: Changed 'timer()' to the correct imported 'time()' alias
    time_before_train = time()

    # Variables for early stopping
    patience_counter = 0
    best_loss = float("inf")

    for epoch in tqdm(range(epochs), desc="Total Epochs"):
        print(f"\nepoch: {epoch}--------------")

        ### Training Step
        train_loss, train_acc = train_step(
            model=model,
            loss_fn=loss_fn,
            optimizer=optimizer,
            accuracy_fn=accuracy_fn,
            data_loader=train_dataloader,
            device=device
        )

        ### Testing Step
        test_loss, test_acc = test_step(
            model=model,
            loss_fn=loss_fn,
            data_loader=test_dataloader,
            accuracy_fn=accuracy_fn,
            device=device
        )
        
        # Ensure tensor values are extracted to primitive float metrics
        if isinstance(train_acc, torch.Tensor): train_acc = train_acc.item()
        if isinstance(test_acc, torch.Tensor): test_acc = test_acc.item()

        ### Apply lr scheduler
        # For CosineAnnealingWarmRestarts, we step per epoch (or batch). No loss metric is passed.
        lr_scheduler.step()

        ### SAVE RESULTS
        training_results['results'].append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_acc": train_acc,
            "test_loss": test_loss,
            "test_acc": test_acc,
        })

        ### Apply early stopping
        if test_loss < best_loss:
            best_loss = test_loss
            patience_counter = 0
            torch.save(model.state_dict(), "best_model.pt")
            print(f"🔥 New best model saved with test loss: {test_loss:.4f}")
        else:
            patience_counter += 1

        if patience_counter >= patience:
            print("🛑 Early stopping triggered")
            break

    # FIX: Changed 'timer()' to 'time()'
    time_after_train = time()

    # FIX: Updated hardcoded "cuda" to the dynamic 'device' parameter
    train_time = print_train_time(time_before_train, time_after_train, device=device)

    ### LOAD THE BEST WEIGHTS BACK IN MEMORY
    model.load_state_dict(torch.load("best_model.pt", weights_only=True))

    ### SAVE METADATA
    training_results["train_time"] = train_time
    training_results["device"] = device
    
    if hasattr(model, "features"):
        training_results["model_layers"] = str(model.features)
    else:
        training_results["model_layers"] = str(type(model))

    return training_results

# SAVE MODEL STATE IN DRIVE
def save_model_results(model: torch.nn.Module,
                       optimizer: torch.optim.Optimizer | None,
                       epochs: int,
                       results: dict,
                       path: str):
    """
    Saves the training checkpoint (model weights, optimizer states, and curves)
    to a designated folder path. Assumes Drive mounting is done in the notebook. 
    [INFO]: To save model state in drive do this before calling this function.
    
    from google.colab import drive
    drive.mount('/content/drive')
    """
    checkpoint = {
        "epochs": epochs,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict() if optimizer is not None else None,
        "results": results
    }

    # save to specified path
    torch.save(checkpoint, path)
    print(f"✅ Checkpoint successfully saved to: {path}")

# LOAD SAVED CHECKPOINT
def load_saved_checkpoint(model: torch.nn.Module,
                          device: torch.device,
                          optimizer: torch.optim.Optimizer | None,
                          path: str,
                          load_trained_params: bool):
    """
    Loads saved metadata and optionally map-restores trained parameters back 
    into memory for testing or resuming training.
    [INFO]: To load from drive do this before calling this function.
    
    from google.colab import drive
    drive.mount('/content/drive')
    """
    # Map-locate to current execution device context
    checkpoint = torch.load(path, map_location=device, weights_only=False)

    if load_trained_params:
        model.load_state_dict(checkpoint["model_state_dict"])

        if optimizer is not None and checkpoint.get("optimizer_state_dict") is not None:
            optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            print("🔄 Loaded both model states and optimizer states!")
        else:
            print("🔄 Loaded model weights only.")

    return checkpoint


# TRAIN MODEL AND TRACK EXPERIMENTS USING TENSORBOARD'S SummaryWriter
def train(model: torch.nn.Module,
          loss_fn: torch.nn.Module,
          optimizer: torch.optim.Optimizer,
          accuracy_fn: Callable,
          train_dataloader: torch.utils.data.DataLoader,
          test_dataloader: torch.utils.data.DataLoader,
          train_step: Callable,
          test_step: Callable,
          print_train_time: Callable,
          lr_scheduler: Callable,
          patience: int,
          epochs: int,
          checkpoint_path: str="best_model.pt",
          device: str=device,
          writer: torch.utils.tensorboard.writer.SummaryWriter=None):

    ### INITIALIZE RESULTS DICTIONARY
    training_results = {
        "results": [],
        "train_time": 0,
        "model_layers": None,
        "device": device
    }

    # FIX: Changed 'timer()' to the correct imported 'time()' alias
    time_before_train = time()

    # Variables for early stopping
    patience_counter = 0
    best_loss = float("inf")

    for epoch in tqdm(range(epochs), desc="Total Epochs"):
        print(f"\nepoch: {epoch}--------------")

        ### Training Step
        train_loss, train_acc = train_step(
            model=model,
            loss_fn=loss_fn,
            optimizer=optimizer,
            accuracy_fn=accuracy_fn,
            data_loader=train_dataloader,
            device=device
        )

        ### Testing Step
        test_loss, test_acc = test_step(
            model=model,
            loss_fn=loss_fn,
            data_loader=test_dataloader,
            accuracy_fn=accuracy_fn,
            device=device
        )

        # Ensure tensor values are extracted to primitive float metrics
        if isinstance(train_acc, torch.Tensor): train_acc = train_acc.item()
        if isinstance(test_acc, torch.Tensor): test_acc = test_acc.item()

        ### Apply lr scheduler
        # For CosineAnnealingWarmRestarts, we step per epoch (or batch). No loss metric is passed.
        if isinstance(
            lr_scheduler,
            torch.optim.lr_scheduler.ReduceLROnPlateau
        ):
            lr_scheduler.step(test_loss)
        else:
            lr_scheduler.step()

        ### SAVE RESULTS
        training_results['results'].append({
            "epoch": epoch,
            "train_loss": train_loss,
            "train_acc": train_acc,
            "test_loss": test_loss,
            "test_acc": test_acc,
        })

        ### TRACK EXPERIMENTS
        if writer is not None:
          writer.add_scalars(main_tag="Loss",
                            tag_scalar_dict={
                                "train_loss": train_loss,
                                "test_loss": test_loss
                            },
                            global_step=epoch)

          writer.add_scalars(main_tag="Accuracy",
                            tag_scalar_dict={
                                "train_acc": train_acc,
                                "test_acc": test_acc
                            },
                            global_step=epoch)

        ### Apply early stopping
        if test_loss < best_loss:
            best_loss = test_loss
            patience_counter = 0
            torch.save(model.state_dict(), "best_model.pt")
            print(f"🔥 New best model saved with test loss: {test_loss:.4f}")
        else:
            patience_counter += 1

        if patience_counter >= patience:
            print("🛑 Early stopping triggered")
            break

    # FIX: Changed 'timer()' to 'time()'
    time_after_train = time()

    # FIX: Updated hardcoded "cuda" to the dynamic 'device' parameter
    train_time = print_train_time(time_before_train, time_after_train, device=device)

    ### LOAD THE BEST WEIGHTS BACK IN MEMORY
    model.load_state_dict(torch.load("best_model.pt", weights_only=True))

    ### SAVE METADATA
    training_results["train_time"] = train_time
    training_results["device"] = device

    if hasattr(model, "features"):
        training_results["model_layers"] = str(model.features)
    else:
        training_results["model_layers"] = str(type(model))

    return training_results

