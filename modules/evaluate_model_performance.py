
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

from timeit import default_timer as timer
from tqdm.auto import tqdm
from typing import Callable, List

import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def evaluate_model_performance(
    model: torch.nn.Module,
    data_loader: torch.utils.data.DataLoader,
    loss_fn: torch.nn.Module,
    accuracy_fn: Callable,
    class_names: List[str],
    display_conf_matrix: bool,
    calculate_flops: Callable | None=None,
    calculate_flops_value: bool=False,
    device: str=device
):
    """
    Evaluates a PyTorch classification model and returns:

    - test loss
    - overall accuracy
    - confusion matrix
    - class-wise accuracy
    - FLOPs (optional)

    [NOTE]: This function needs calfops library's calculate_flops function if you want to calculate FLOPs.
    You can install by running the following script before calling this function

    try:
      from calflops import calculate_flops
    except:
      !pip install calflops
      from calflops import calculate_flops


    [NOTE]: This function needs accuracy function and if you want pytorch-ignite's accuracy function,
    ignite accuracy_fn supports update, reset functions used in this function
    You can install by running the following script before calling this function

    try:
      from ignite.metrics import Accuracy
    except:
      !pip install pytorch-ignite
      from ignite.metrics import Accuracy
    accuracy_fn = Accuracy()


    Args:
        model: Trained PyTorch model.
        data_loader: Test/validation DataLoader.
        loss_fn: Loss function.
        accuracy_fn: Accuracy function.
        class_names: List of class names in the same order as model classes.
        calculate_flops_value: Whether to calculate FLOPs.
        calculate_flops: to calculate FLOPS

    Returns:
        Dictionary containing evaluation results.
    """

    ### 1. EVALUATE THE MODEL

    model.eval()
    accuracy_fn.reset()

    total_loss = 0

    # Store predictions and true labels
    all_preds = []
    all_labels = []

    with torch.inference_mode():

        for X, y in tqdm(data_loader):

            X = X.to(device)
            y = y.to(device)

            y_preds = model(X)

            # Extract logits if model returns an object containing logits
            if hasattr(y_preds, "logits"):
                logits = y_preds.logits
            else:
                logits = y_preds

            # Loss
            loss_batch = loss_fn(logits, y)
            total_loss += loss_batch.item()

            # Overall accuracy
            accuracy_fn.update((logits, y))

            # Predictions
            preds = torch.argmax(logits, dim=1)

            # Save predictions and labels
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(y.cpu().numpy())

    # Average loss
    loss = total_loss / len(data_loader)

    # Overall accuracy
    accuracy = accuracy_fn.compute()

    # Convert to numpy arrays
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)

    ### 2. CONFUSION MATRIX
    cm = confusion_matrix(
        all_labels,
        all_preds,
        labels=list(range(len(class_names)))
    )

    # Display confusion matrix by count each sample image
    if display_conf_matrix:

      conf_matrix_count_disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                                      display_labels=class_names)

      fig, ax = plt.subplots(figsize=(8,8))
      conf_matrix_count_disp.plot(ax=ax, cmap="Blues", values_format="d")

      plt.xticks(rotation=45)
      plt.title("Confusion Matrix")
      plt.show()

      conf_matrix_proportion_disp = ConfusionMatrixDisplay.from_predictions(all_labels,
                                                                            all_preds,
                                                                            display_labels=class_names,
                                                                            normalize="true",
                                                                            cmap="Blues",
                                                                            values_format=".2f")
      plt.xticks(rotation=45)
      plt.title("Normalized Confusion Matrix")
      plt.show()

    ### 3. CLASS-WISE ACCURACY
    classwise_accuracy = {}

    for i in range(len(cm)):

        total_actual = cm[i].sum()

        if total_actual > 0:
            class_acc = cm[i, i] / total_actual
        else:
            class_acc = 0.0

        classwise_accuracy[class_names[i]] = float(class_acc)

    ### 4. FLOPs
    flops_result = None
    if calculate_flops_value:
      # throw error of calculate_flops is not supplied to function 
      if calculate_flops is None:
        raise ValueError(
            "calculate_flops must be provided when "
            "calculate_flops_value=True."
        )

      # Get one batch only to determine input shape
      sample_X, _ = next(iter(data_loader))
      sample_X = sample_X[:1].to(device)

      flops_result = calculate_flops(model=model,
                                     input_shape=tuple(sample_X.shape)) # we can also hardcode the shape as (1, 3, 224, 224)

    return {
        "model_name": model.__class__.__name__,
        "loss": loss,
        "accuracy": accuracy,
        "confusion_matrix": cm,
        "classwise_accuracy": classwise_accuracy,
        "y_true": all_labels,
        "y_pred": all_preds,
        "flops": flops_result,
    }
