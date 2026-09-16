
import torch
import torchvision
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import os

# NUM_WORKERS = os.cpu_count()

device = "cuda" if torch.cuda.is_available() else "cpu"

PIN_MEMORY = True if device == "cuda" else False

def create_dataloaders(train_dir: str,
                       test_dir: str,
                       batch_size: int,
                       train_transform: transforms.Compose=None,
                       test_transform: transforms.Compose=None,
                      #  num_workers: int=NUM_WORKERS,
                       pin_memory: bool=PIN_MEMORY):
  if train_transform is None or test_transform is None:
    print(f"[INFO] train and test transform both need to be passed. Exitting...")
    return None, None, None

  train_dataset = datasets.ImageFolder(root=train_dir,
                                       transform=train_transform)
  test_dataset = datasets.ImageFolder(root=test_dir,
                                      transform=test_transform)

  train_dataloader = DataLoader(dataset=train_dataset,
                                batch_size=batch_size,
                                shuffle=True,
                                pin_memory=pin_memory)

  test_dataloader = DataLoader(dataset=test_dataset,
                               batch_size=batch_size,
                               shuffle=False,
                               pin_memory=pin_memory)

  classes = train_dataset.classes
  return train_dataloader, test_dataloader, classes, train_dataset, test_dataset
