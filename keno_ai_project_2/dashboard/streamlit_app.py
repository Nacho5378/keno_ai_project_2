import streamlit as st
from keno_core.analyzer import get_hot_cold_numbers
from keno_core.predictor import predict_next_draw
from keno_core.ticket_gen import generate_ticket
from ocr.extractor import extract_numbers_from_image
import pandas as pd
import os

st.set_page_config(page_title="Keno AI Dashboard", layout="wide")

st.title("🎰 Keno AI Dashboard")
tabs = st.tabs(["📷 OCR", "🔥 Hot/Cold Analysis", "🤖 AI Prediction", "🎟️ Ticket Generator"])

# Load the dataset if available
data_path = os.path.join("data", "keno_draws.csv")
draws_df = pd.read_csv(data_path) if os.path.exists(data_path) else pd.DataFrame()

# 📷 OCR Tab
with tabs[0]:
    st.header("OCR: Extract Drawn Numbers from Image")
    uploaded_file = st.file_uploader("Upload Keno result image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        numbers = extract_numbers_from_image(uploaded_file)
        st.success(f"Extracted Numbers: {numbers}")

# 🔥 Hot/Cold Tab
with tabs[1]:
    st.header("Hot/Cold Number Analysis")
    if not draws_df.empty:
        hot, cold = get_hot_cold_numbers(draws_df)
        st.subheader("🔥 Hot Numbers")
        st.write(hot)
        st.subheader("❄️ Cold Numbers")
        st.write(cold)
    else:
        st.warning("Please add 'keno_draws.csv' to the data/ folder.")

# 🤖 AI Prediction Tab
with tabs[2]:
    st.header("AI-Based Next Draw Prediction")
    if not draws_df.empty:
        prediction = predict_next_draw(draws_df)
        st.success(f"Predicted Numbers: {prediction}")
    else:
        st.warning("Please add 'keno_draws.csv' to the data/ folder.")

# 🎟️ Ticket Generator Tab
with tabs[3]:
    st.header("Generate a Random Keno Ticket")
    num_spots = st.slider("Number of Spots (numbers to play)", 1, 20, 10)
    ticket = generate_ticket(num_spots)
    st.success(f"Your Ticket: {ticket}")