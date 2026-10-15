train_transform_aug_6 = transforms.Compose([
    # 1. Convert to 3 channels first
    transforms.Grayscale(num_output_channels=3),

    # 2. Aggressive Geometric Distortions (Applied at native resolution)
    transforms.RandomAffine(
        degrees=35,                 # INCREASED from 20: Heavy head tilts and side angles
        translate=(0.15, 0.15),     # INCREASED from 0.10: Off-center faces to handle poor framing
        scale=(0.80, 1.20),         # EXPANDED from 0.9-1.1: Aggressive zooming in and out
        shear=12,                   # INCREASED from 5: Heavy perspective warping
        interpolation=InterpolationMode.BILINEAR,
        fill=124                    # Fills empty corners with ImageNet gray
    ),

    # 3. Random Perspective (New addition for maximum aggressiveness)
    # Simulates faces looking drastically up, down, or from extreme side profiles
    transforms.RandomPerspective(distortion_scale=0.4, p=0.5, interpolation=InterpolationMode.BILINEAR, fill=124),

    transforms.RandomHorizontalFlip(p=0.5),

    # 4. Upscale after applying all geometric changes
    transforms.Resize((224, 224), interpolation=InterpolationMode.BILINEAR),

    # 5. Intense Illumination & Blur Changes
    transforms.ColorJitter(
        brightness=0.35,            # INCREASED from 0.15: Simulates heavy shadows / overexposure
        contrast=0.35               # INCREASED from 0.15: Drastic lighting drops
    ),

    # Simulates blurry or low-quality webcam/security camera images
    transforms.GaussianBlur(kernel_size=(5, 5), sigma=(0.1, 2.0)),

    transforms.ToTensor(),

    # 6. Aggressive Random Erasing (Cutout)
    transforms.RandomErasing(
        p=0.50,                     # INCREASED from 0.25: Happens to every second image now
        scale=(0.02, 0.20),         # INCREASED max from 0.10: Can completely mask the eyes or mouth
        ratio=(0.3, 3.3),
        value='random'
    ),

    # 7. Normalize
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

## datat loader for this transform
(train_dataloader_aug_6, test_dataloader, class_names, train_dataset_aug_6, test_dataset) =  create_dataloaders.create_dataloaders(train_dir=train_dir,
                   test_dir=test_dir,
                   batch_size=64,
                   train_transform=train_transform_aug_6,
                   test_transform=transform)