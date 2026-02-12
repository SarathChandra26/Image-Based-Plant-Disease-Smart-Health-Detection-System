def analyze_health(features, confidence):
    results = {}

    # Early stress detection
    if features["yellow_ratio"] > 0.18 and confidence < 0.6:
        results["Early Stress"] = "Detected"
    else:
        results["Early Stress"] = "Not detected"

    # Water
    if features["green_ratio"] < 0.4:
        results["Water Stress"] = "Low water detected"
    else:
        results["Water Stress"] = "Normal"

    # Sunlight
    if features["brown_ratio"] > 0.15:
        results["Sunlight"] = "Excess exposure"
    else:
        results["Sunlight"] = "Optimal"

    # Nutrients
    if features["yellow_ratio"] > 0.25:
        results["Nutrient Risk"] = "Nitrogen deficiency"
    else:
        results["Nutrient Risk"] = "Normal"

    # Pest
    if features["brown_ratio"] > 0.2:
        results["Pest Damage"] = "Present"
    else:
        results["Pest Damage"] = "Not detected"

    # Disease
    if confidence > 0.7:
        results["Disease Status"] = "Detected"
    else:
        results["Disease Status"] = "Uncertain"

    return results
