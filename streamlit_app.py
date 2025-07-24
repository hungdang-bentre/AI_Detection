import streamlit as st
import joblib

model = joblib.load('ai_text_classifier.pkl')

st.title("🤖 AI vs Human Text Classifier")
user_input = st.text_area("Nhập đoạn văn để kiểm tra", height=200)

if user_input:
    result = model.predict([user_input])[0]
    st.success(f"Kết quả: {'AI 🧠' if result == 1.0 else 'Human 👤'}")
