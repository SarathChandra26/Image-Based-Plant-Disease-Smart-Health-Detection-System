import os
import shutil
import random

RAW_DIR = "data/raw/PlantVillage"
TRAIN_DIR = "data/processed/train"
VAL_DIR = "data/processed/val"

CLASSES = {
    "Tomato_healthy": "Healthy",
    "Tomato_Early_blight": "Early_Blight",
    "Tomato_Late_blight": "Late_Blight",
    "Tomato_Leaf_Mold": "Leaf_Mold",
    "Potato___Early_blight": "Potato_Early_Blight",
    "Potato___Late_blight": "Potato_Late_Blight"
}

SPLIT_RATIO = 0.8

for src_class, dst_class in CLASSES.items():
    src_path = os.path.join(RAW_DIR, src_class)

    images = os.listdir(src_path)
    random.shuffle(images)

    split = int(len(images) * SPLIT_RATIO)
    train_imgs = images[:split]
    val_imgs = images[split:]

    for img in train_imgs:
        shutil.copy(
            os.path.join(src_path, img),
            os.path.join(TRAIN_DIR, dst_class, img)
        )

    for img in val_imgs:
        shutil.copy(
            os.path.join(src_path, img),
            os.path.join(VAL_DIR, dst_class, img)
        )

print("Dataset split completed successfully.")
