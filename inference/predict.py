import tensorflow as tf
import cv2
import numpy as np

MODEL_PATH = "models/plant_disease_model.h5"
IMG_SIZE = (224, 224)

CLASS_NAMES = [
    "Healthy",
    "Early_Blight",
    "Late_Blight",
    "Leaf_Mold",
    "Potato_Early_Blight",
    "Potato_Late_Blight"
]

model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, IMG_SIZE)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = preds[0][class_id]

    return CLASS_NAMES[class_id], float(confidence)

if __name__ == "__main__":
    path = input("Enter image path: ")
    disease, conf = predict_image(path)
    print(f"Disease: {disease}")
    print(f"Confidence: {conf:.2f}")
