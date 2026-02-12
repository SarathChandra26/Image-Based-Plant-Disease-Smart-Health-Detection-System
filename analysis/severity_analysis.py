import cv2
import numpy as np

def analyze_damage(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Detect brown/yellow damaged regions
    brown_mask = (hsv[:, :, 2] < 100)
    yellow_mask = (hsv[:, :, 0] > 20) & (hsv[:, :, 0] < 35)

    damage_mask = brown_mask | yellow_mask

    total_pixels = img.shape[0] * img.shape[1]
    damaged_pixels = np.sum(damage_mask)

    damage_ratio = damaged_pixels / total_pixels

    # Create visualization
    overlay = img.copy()
    overlay[damage_mask] = [0, 0, 255]  # red highlight

    return round(damage_ratio * 100, 2), overlay


def calculate_severity(damage_percent):
    if damage_percent < 10:
        return "Early"
    elif damage_percent < 30:
        return "Moderate"
    else:
        return "Severe"
