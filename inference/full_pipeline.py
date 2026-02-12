from inference.predict import predict_image
from analysis.feature_extraction import extract_features
from rules.health_rules import analyze_health
from scoring.health_score import calculate_health_score
from rules.recommendation_engine import generate_recommendations, care_urgency
from analysis.severity_analysis import analyze_damage, calculate_severity
from analysis.explainability import explain_decision


def run_pipeline(image_path):
    # 1. Disease prediction
    disease, confidence = predict_image(image_path)

    # 2. Feature extraction
    features = extract_features(image_path)

    # 3. Health rule analysis
    results = analyze_health(features, confidence)

    # 4. Health score
    health_score = calculate_health_score(results)

    # 5. Leaf damage & severity
    damage_percent, _ = analyze_damage(image_path)
    severity = calculate_severity(damage_percent)

    # 6. Recommendations & priority
    actions, priority = generate_recommendations(results, health_score)

    # 7. Care urgency
    urgency = care_urgency(health_score, severity)

    # 8. Explainability
    explanations = explain_decision(features, confidence, damage_percent)

    # -------- OUTPUT --------
    print("\nDisease Detected:", disease)
    print("Severity Level:", severity)
    print(f"Prediction Confidence: {confidence*100:.0f}%\n")

    print(f"Plant Health Score: {health_score} / 100")
    print(f"Care Priority: {priority}")
    print(f"Care Urgency: {urgency}\n")

    print(f"Leaf Area Damage: {damage_percent}%\n")

    for k, v in results.items():
        print(f"{k}: {v}")

    print("\nExplainability:")
    for r in explanations:
        print("-", r)

    print("\nRecommended Actions:")
    for act in actions:
        print("•", act)


if __name__ == "__main__":
    img = input("Enter image path: ")
    run_pipeline(img)
