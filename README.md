# 🧠 Parkinson Disease Detection using Machine Learning

## 📌 Overview

This project aims to detect Parkinson’s Disease using voice-based features.
We built an Artificial Neural Network (ANN) model that analyzes vocal characteristics and predicts whether a person is healthy or affected by Parkinson’s disease.

---

## ❓ Problem Statement

Parkinson’s Disease is a neurological disorder that affects movement and speech.
Early detection is difficult but crucial.

The goal of this project is to:

* Use voice measurements as input features
* Build a machine learning model
* Predict whether a person has Parkinson’s or not

---

## 📊 Dataset

The dataset contains biomedical voice measurements from patients.

### Key Features:

* **Fo (Fundamental Frequency)** – voice pitch
* **Jitter (%)** – variation in frequency
* **Shimmer** – variation in amplitude
* **HNR (Harmonic-to-Noise Ratio)** – voice clarity

📌 Note:
The dataset is included for transparency, but the trained model is used directly for predictions.

---

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* TensorFlow / Keras (ANN)
* Streamlit (Web App)

---

## 🔄 Project Workflow

1. Data Loading
2. Data Preprocessing
3. Feature Scaling (StandardScaler)
4. Model Building (ANN)
5. Model Training
6. Model Evaluation
7. Saving Model (.h5) & Scaler (.pkl)
8. Deployment using Streamlit

---

## 🧠 Model Details

* Input Layer: 4 features
* Hidden Layers: Dense layers with ReLU activation
* Dropout used to prevent overfitting
* Output Layer: Sigmoid (Binary Classification)

---

## 📈 Results

* Model achieved ~80% accuracy
* Training and validation loss decreased steadily
* Model performs well on voice-based prediction

---

## 🌐 Streamlit Web App

The project includes an interactive web application where users can:

* Input voice feature values
* Get instant prediction
* View result as Healthy or Parkinson Detected

---

## ▶️ How to Run

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the app

```bash
streamlit run app.py
```

## 📌 Conclusion

This project demonstrates that voice-based features can effectively be used to detect Parkinson’s Disease.
Higher jitter and shimmer values indicate instability, while lower HNR reflects reduced voice clarity.

---

## 👨‍💻 Author

Pranav Thakur
