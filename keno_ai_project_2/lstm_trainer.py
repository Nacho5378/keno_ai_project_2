import pandas as pd
import numpy as np
import tensorflow as tf
import os

DATA_PATH = os.path.join("data", "keno_draws.csv")
MODEL_SAVE_PATH = os.path.join("models", "lstm_model.h5")

def preprocess_sequences(draws_df, seq_len=10):
    draws = draws_df.values.tolist()
    X, y = [], []
    for i in range(len(draws) - seq_len):
        seq = draws[i:i + seq_len]
        target = draws[i + seq_len]
        X.append(np.array(seq).flatten())
        y.append(np.zeros(81))
        for num in target:
            y[-1][num - 1] = 1

    X = np.array(X).reshape((-1, seq_len * 20, 1))
    y = np.array(y)
    return X, y

def train_lstm_model():
    draws_df = pd.read_csv(DATA_PATH)
    X, y = preprocess_sequences(draws_df)

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X.shape[1], 1)),
        tf.keras.layers.LSTM(128, return_sequences=False),
        tf.keras.layers.Dense(81, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(X, y, epochs=10, batch_size=32)
    model.save(MODEL_SAVE_PATH)

if __name__ == "__main__":
    train_lstm_model()
