# -------- VERY IMPORTANT: PATH FIX (MUST BE FIRST) --------
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

# -------- NOW SAFE TO IMPORT --------
import streamlit as st
from inference.predict import predict_image
from analysis.feature_extraction import extract_features
from rules.health_rules import analyze_health
from scoring.health_score import calculate_health_score
from rules.recommendation_engine import generate_recommendations, care_urgency
from analysis.severity_analysis import analyze_damage, calculate_severity
from analysis.explainability import explain_decision
from PIL import Image
import tempfile

# -------- STREAMLIT UI --------
st.set_page_config(page_title="Plant Health AI", layout="centered")

st.title("🌿 Image-Based Plant Health Detection System")
st.write("Upload a plant leaf image to analyze disease and health status.")

uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        image_path = tmp.name

    image = Image.open(image_path)
    st.image(image, caption="Uploaded Leaf Image", use_column_width=True)

    st.markdown("---")
    st.subheader("🔍 Analysis Result")

    # -------- PIPELINE --------
    disease, confidence = predict_image(image_path)
    features = extract_features(image_path)
    results = analyze_health(features, confidence)
    health_score = calculate_health_score(results)

    damage_percent, _ = analyze_damage(image_path)
    severity = calculate_severity(damage_percent)

    actions, priority = generate_recommendations(results, health_score)
    urgency = care_urgency(health_score, severity)
    explanations = explain_decision(features, confidence, damage_percent)

    # -------- OUTPUT --------
    st.markdown(f"### 🦠 Disease Detected: **{disease}**")
    st.markdown(f"- **Prediction Confidence:** {confidence*100:.0f}%")
    st.markdown(f"- **Severity Level:** {severity}")

    st.markdown("### 📊 Health Overview")
    st.markdown(f"- **Health Score:** {health_score} / 100")
    st.markdown(f"- **Care Priority:** {priority}")
    st.markdown(f"- **Care Urgency:** {urgency}")
    st.markdown(f"- **Leaf Area Damage:** {damage_percent}%")

    st.markdown("### 🌱 Detected Conditions")
    for k, v in results.items():
        st.markdown(f"- **{k}:** {v}")

    st.markdown("### 🔍 Explainability")
    for r in explanations:
        st.markdown(f"- {r}")

    st.markdown("### 🛠️ Recommended Actions")
    for act in actions:
        st.markdown(f"- {act}")

    os.remove(image_path)
