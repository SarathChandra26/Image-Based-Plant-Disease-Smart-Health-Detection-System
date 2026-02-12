import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

IMG_SIZE = (224, 224)
BATCH_SIZE = 16

MODEL_PATH = "models/plant_disease_model.h5"
VAL_DIR = "data/processed/val"

model = tf.keras.models.load_model(MODEL_PATH)

val_datagen = ImageDataGenerator(rescale=1./255)

val_gen = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

preds = model.predict(val_gen)
y_pred = np.argmax(preds, axis=1)
y_true = val_gen.classes

print("\nClassification Report:\n")
print(classification_report(y_true, y_pred, target_names=val_gen.class_indices.keys()))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_true, y_pred))
