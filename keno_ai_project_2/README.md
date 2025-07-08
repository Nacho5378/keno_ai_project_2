# 🎰 Keno AI Project

An AI-powered dashboard for Keno draw prediction and analysis. Built with Streamlit, EasyOCR, and TensorFlow.

## 🧩 Features

- 📷 OCR Extraction: Extract drawn numbers from Keno result images.
- 🔥 Hot/Cold Analysis: Identify the most and least frequent numbers.
- 🤖 AI Prediction: Predict next draw numbers using LSTM (or fallback to random if model isn't trained).
- 🎟️ Ticket Generator: Create a randomized playable Keno ticket.

## 📁 Folder Structure

```
keno_ai_project/
├── dashboard/              # Streamlit dashboard
├── keno_core/              # Analysis, prediction, and ticket generator logic
├── ocr/                    # OCR logic using EasyOCR
├── data/                   # Contains keno_draws.csv (historical data)
├── models/                 # Trained LSTM model (lstm_model.h5)
└── lstm_trainer.py         # LSTM training script
```

## 🚀 Deployment

1. Upload to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and deploy from your GitHub repo.
3. Set the entry file to: `dashboard/streamlit_app.py`

## ⚙️ Requirements

Install with:

```bash
pip install -r requirements.txt
```

## 🧠 Train the AI Model (Optional)

To train the LSTM predictor, run:

```bash
python lstm_trainer.py
```

Make sure `data/keno_draws.csv` contains enough historical draw data.

---

Happy predicting! 🎲
