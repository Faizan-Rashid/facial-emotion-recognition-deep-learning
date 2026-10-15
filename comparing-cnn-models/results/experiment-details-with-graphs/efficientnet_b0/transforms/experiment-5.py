from timm.data.auto_augment import rand_augment_transform
from timm.data.transforms import RandomResizedCropAndInterpolation

train_transform_aug_1 = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    rand_augment_transform(
    config_str='rand-m4-mstd0.25',
    # hparams={'translate_const': 117, 'img_mean': (124, 116, 104)}
    ),
    RandomResizedCropAndInterpolation(size=224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

train_dataset_1 = torchvision.datasets.ImageFolder(
    root=train_dir,
    transform=train_transform_aug_1
)

train_dataloader_aug_1 = DataLoader(
    dataset=train_dataset_1,
    batch_size=32,
    shuffle=True,
    pin_memory=False
)