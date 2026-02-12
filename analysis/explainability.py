def explain_decision(features, confidence, damage_percent):
    reasons = []

    if features["yellow_ratio"] > 0.25:
        reasons.append("High yellow pixel ratio detected")

    if features["brown_ratio"] > 0.2:
        reasons.append("Presence of brown/damaged regions")

    if confidence > 0.7:
        reasons.append("High disease prediction confidence")

    if damage_percent > 20:
        reasons.append("Large infected leaf area")

    return reasons
