def calculate_health_score(results):
    score = 100

    if results["Disease Status"] == "Detected":
        score -= 40

    if results["Water Stress"] != "Normal":
        score -= 15

    if results["Sunlight"] != "Optimal":
        score -= 10

    if results["Nutrient Risk"] != "Normal":
        score -= 15

    if results["Pest Damage"] == "Present":
        score -= 20

    return max(score, 0)
