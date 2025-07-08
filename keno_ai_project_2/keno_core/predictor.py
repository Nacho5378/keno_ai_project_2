import numpy as np
import tensorflow as tf
import os
import random

MODEL_PATH = os.path.join("models", "lstm_model.h5")

def predict_next_draw(draws_df, num_predictions=20):
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
        seq = draws_df.tail(10).values.flatten()
        seq = np.array(seq[-100:]).reshape(1, -1, 1)
        prediction = model.predict(seq)[0]
        return list(np.argsort(prediction)[-num_predictions:][::-1])
    else:
        return sorted(random.sample(range(1, 81), num_predictions))
