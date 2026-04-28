import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Load model & scaler
model = load_model("ann_model.h5")
scaler = pickle.load(open("scaler.pkl", "rb"))

# UI
st.set_page_config(page_title="Parkinson Detection", page_icon="🧠")
st.title("🧠 Parkinson Disease Detection")

col1, col2 = st.columns(2)

fo = col1.slider("Frequency (Fo Hz)", 80.0, 300.0, 120.0)
jitter = col1.slider("Jitter (%)", 0.0, 0.05, 0.005, step=0.001)

shimmer = col2.slider("Shimmer", 0.0, 0.1, 0.03, step=0.001)
hnr = col2.slider("HNR", 0.0, 40.0, 20.0, step=0.5)

if st.button("🔍 Predict"):
    data = scaler.transform([[fo, jitter, shimmer, hnr]])
    result = model.predict(data)[0][0]

    if result > 0.5:
        st.error("❌ Parkinson Detected")
    else:
        st.success("✅ Healthy")
