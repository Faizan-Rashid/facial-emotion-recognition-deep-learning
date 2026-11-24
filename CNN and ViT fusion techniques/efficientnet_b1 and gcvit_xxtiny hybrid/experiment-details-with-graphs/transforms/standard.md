Standard transform

### the augumentation pipeline
train_transform_aug = transforms.Compose([

    transforms.Resize((224,224)),

    # MobileNet expects 3 channels
    transforms.Grayscale(num_output_channels=3),

    # Geometric augmentations
    transforms.RandomAffine(
        degrees=20,
        translate=(0.1,0.1),
        scale=(0.9,1.1),
        shear=5,
        interpolation=InterpolationMode.BILINEAR
    ),

    transforms.RandomHorizontalFlip(0.5),

    # Illumination augmentations
    transforms.ColorJitter(
        brightness=0.15,
        contrast=0.15
    ),

    transforms.ToTensor(),

    # Cutout / Random Erasing
    transforms.RandomErasing(
        p=0.25,
        scale=(0.02,0.10),
        ratio=(0.3,3.3),
        value='random'      # <-- before Normalize
    ),

    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])