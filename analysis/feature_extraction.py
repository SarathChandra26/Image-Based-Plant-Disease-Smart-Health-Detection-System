import cv2
import numpy as np

def extract_features(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))

    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    total_pixels = img.shape[0] * img.shape[1]

    green_mask = (hsv[:, :, 1] > 40) & (hsv[:, :, 2] > 40)
    yellow_mask = (hsv[:, :, 0] > 20) & (hsv[:, :, 0] < 35)
    brown_mask = (hsv[:, :, 0] < 20) & (hsv[:, :, 2] < 100)

    green_ratio = np.sum(green_mask) / total_pixels
    yellow_ratio = np.sum(yellow_mask) / total_pixels
    brown_ratio = np.sum(brown_mask) / total_pixels

    return {
        "green_ratio": round(green_ratio, 2),
        "yellow_ratio": round(yellow_ratio, 2),
        "brown_ratio": round(brown_ratio, 2)
    }
