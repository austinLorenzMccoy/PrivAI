#save_model.py
import joblib
from tensorflow.keras.models import load_model

def save_models(vectorizer, label_encoder, svm_model, nb_model, lstm_model):
    # Save the vectorizer and label encoder
    joblib.dump(vectorizer, 'models/tfidf_vectorizer.joblib')
    joblib.dump(label_encoder, 'models/label_encoder.joblib')

    # Save SVM and Naive Bayes models
    joblib.dump(svm_model, 'models/svm_model.joblib')
    joblib.dump(nb_model, 'models/naive_bayes_model.joblib')

    # Save the LSTM model as .h5
    lstm_model.save('models/lstm_model.h5')
