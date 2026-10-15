
from timm.data.auto_augment import auto_augment_transform
from timm.data.transforms import RandomResizedCropAndInterpolation

train_transform_aug_4 =  transforms.Compose([
    # Convert grayscale image to 3 channels
    transforms.Grayscale(num_output_channels=3),

    # Mild random crop + resize
    RandomResizedCropAndInterpolation(
        size=224,
        scale=(0.85, 1.0),
        ratio=(0.95, 1.05)
    ),

    # Horizontal facial symmetry
    transforms.RandomHorizontalFlip(p=0.5),

    # Small changes in head orientation
    transforms.RandomRotation(degrees=10),

    # timm AutoAugment
   rand_augment_transform(
    config_str='rand-m10-mstd0.5',
    hparams={'translate_const': 117, 'img_mean': (124, 116, 104)}
    ),

    transforms.ToTensor(),

    # ImageNet normalization for pretrained EfficientNet
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

train_dataset_4 = torchvision.datasets.ImageFolder(
    root=train_dir,
    transform=train_transform_aug_4
)

train_dataloader_aug_4 = DataLoader(
    dataset=train_dataset_4,
    batch_size=64,
    shuffle=True,
    pin_memory=False
)