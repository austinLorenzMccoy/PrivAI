# load_models.py
import joblib
from tensorflow.keras.models import load_model

def load_models():
    try:
        # Load the vectorizer and label encoder
        vectorizer = joblib.load('models/tfidf_vectorizer.joblib')
        label_encoder = joblib.load('models/label_encoder.joblib')

        # Load SVM and Naive Bayes models
        svm_model = joblib.load('models/svm_model.joblib')
        nb_model = joblib.load('models/naive_bayes_model.joblib')

        # Load the LSTM model
        lstm_model = load_model('models/lstm_model.h5')

        print("All models loaded successfully.")
        return vectorizer, label_encoder, svm_model, nb_model, lstm_model
    except Exception as e:
        print(f"Error loading models: {e}")
