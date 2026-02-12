def generate_recommendations(results, health_score):
    actions = []

    # Disease management (robust check)
    disease_status = results.get("Disease Status", "").lower()
    if "detected" in disease_status:
        actions.append("Isolate affected plant if possible")
        actions.append("Apply appropriate fungicide as per disease type")
        actions.append("Remove severely infected leaves")

    # Water
    if results.get("Water Stress") != "Normal":
        actions.append("Water plant immediately")

    # Sunlight
    if results.get("Sunlight") != "Optimal":
        actions.append("Move to partial shade")

    # Nutrients
    if results.get("Nutrient Risk") != "Normal":
        actions.append("Add compost or organic fertilizer")

    # Pests
    if results.get("Pest Damage") == "Present":
        actions.append("Inspect leaves for pests and treat accordingly")

    # Care priority
    if health_score < 50:
        priority = "HIGH"
    elif health_score < 75:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return actions, priority
#Care Urgency Timer 
def care_urgency(health_score, severity):
    if severity == "Severe" or health_score < 40:
        return "Immediate (within 24 hours)"
    elif severity == "Moderate":
        return "Soon (within 48 hours)"
    else:
        return "Monitor (3–5 days)"
