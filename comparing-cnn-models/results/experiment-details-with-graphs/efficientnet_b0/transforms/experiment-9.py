from torchvision.transforms import InterpolationMode

### augmentation pipeline
train_transform_aug_5 = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),

    transforms.RandomAffine(
        degrees=25,
        translate=(0.10, 0.10),
        scale=(0.85, 1.15),
        shear=7,
        interpolation=InterpolationMode.BILINEAR,
        fill=124
    ),

    transforms.RandomPerspective(
        distortion_scale=0.25,
        p=0.3,
        interpolation=InterpolationMode.BILINEAR,
        fill=124
    ),

    transforms.RandomHorizontalFlip(p=0.5),

    transforms.Resize(
        (224, 224),
        interpolation=InterpolationMode.BILINEAR
    ),

    transforms.ColorJitter(
        brightness=0.28,
        contrast=0.28
    ),

    transforms.GaussianBlur(
        kernel_size=(5, 5),
        sigma=(0.1, 1.5)
    ),

    transforms.ToTensor(),

    transforms.RandomErasing(
        p=0.40,
        scale=(0.02, 0.15),
        ratio=(0.3, 3.3),
        value="random"
    ),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
(train_dataloader_aug_5, test_dataloader, class_names, train_dataset_aug_5, test_dataset) =  create_dataloaders.create_dataloaders(train_dir=train_dir,
                   test_dir=test_dir,
                   batch_size=64,
                   train_transform=train_transform_aug_5,
                   test_transform=transform)