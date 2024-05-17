import joblib

def classify(text):
    '''
    This function classify resume by providing extracted text
    '''
    vectorizer = joblib.load('models/classification/tfidf_vectorizer.pkl')

    saved_model = joblib.load('models/classification/rf_classifier_model.pkl')

    new_data_tfidf = vectorizer.transform([text])

    return saved_model.predict(new_data_tfidf)[0]