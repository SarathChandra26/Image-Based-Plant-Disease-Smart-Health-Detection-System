# 🌿 Image-Based Plant Disease & Smart Health Detection System

An **offline AI-powered plant health analysis system** that detects leaf diseases using deep learning and generates explainable health insights with actionable recommendations.

This project integrates **CNN-based disease classification (MobileNetV2 transfer learning)** with **computer vision damage quantification and rule-based reasoning**, deployed via a Streamlit interface for real-time agricultural decision support.

---

## 🚀 Key Features

### 🧠 Deep Learning Disease Detection

* Transfer Learning using **MobileNetV2**
* Multi-class disease classification
* Confidence-aware prediction
* Fully offline inference (no APIs)

### 📊 Smart Health Analysis

* Leaf area damage percentage estimation
* Severity classification (Early / Moderate / Severe)
* Health score calculation (0–100)
* Care priority (Low / Medium / High)
* Care urgency estimation (time-based)

### 🌱 Environmental & Stress Detection

* Water stress indicators
* Sunlight exposure analysis
* Nutrient deficiency risk estimation
* Pest damage detection
* Early stress warning (preventive monitoring)

### 🔍 Explainable AI Layer

* Rule-based reasoning engine
* Transparent decision explanation
* Non-hallucinated logic-based outputs

### 🖥 Streamlit User Interface

* Image upload support
* Real-time analysis
* Structured health report output
* Fully offline deployment

---

## 🏗 System Architecture

```
Leaf Image
    ↓
MobileNetV2 (Transfer Learning)
    ↓
Disease Prediction + Confidence
    ↓
OpenCV Feature Extraction
    ↓
Damage % + Severity Estimation
    ↓
Rule-Based Health Analysis
    ↓
Health Score + Priority + Urgency
    ↓
Explainability + Recommendations
    ↓
Streamlit UI Output
```

---

## 🛠 Tech Stack

* Python
* TensorFlow / Keras
* OpenCV
* NumPy
* Scikit-learn
* Streamlit
* Transfer Learning (MobileNetV2)

---

## 📦 Dataset

* PlantVillage Dataset (selected classes)
* 80/20 train-validation split
* Data augmentation applied
* Model trained using transfer learning from ImageNet weights

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Image-Based-Plant-Disease-Smart-Health-Detection-System.git
cd Image-Based-Plant-Disease-Smart-Health-Detection-System
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit App

```bash
streamlit run ui/app.py
```

Then open:

```
http://localhost:8501
```

---

## 📈 Model Overview

* Architecture: MobileNetV2 (pretrained on ImageNet)
* Custom classification head
* Frozen base layers during training
* Optimized for CPU inference
* Suitable for mobile deployment (TFLite convertible)

---

## 🔮 Future Scope

* TensorFlow Lite conversion for Android offline deployment
* Real-time camera integration
* Disease heatmap visualization
* Multi-crop adaptive threshold tuning
* Edge-device optimization

Developed By 
Ummadishetty Sarath Chandra

