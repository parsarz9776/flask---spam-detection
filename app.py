from flask import Flask, render_template, request, jsonify
import pickle
import spacy
from nltk.stem import PorterStemmer
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load your saved model
with open('models/model_pickle', 'rb') as f:
    model = pickle.load(f)

# Load the vectorizer
with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load spaCy for text processing
nlp = spacy.load('en_core_web_sm')

# Function for text preprocessing
def preprocess(text):
    doc = nlp(text)
    no_stop_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(no_stop_words)

# Function for stemming
def stemmer(text):
    text = text.split()
    words = ''
    stemmer = PorterStemmer()
    for i in text:
        words += (stemmer.stem(i)) + ' '
    return words.strip()

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Get the input text from the form
            input_text = request.form['text']

            # Preprocess and stem the input text
            processed_text = preprocess(input_text)
            stemmed_text = stemmer(processed_text)

            # Vectorize the input text using the CountVectorizer fitted on the training data
            vectorized_text = vectorizer.transform([stemmed_text])

            # Make prediction
            prediction = model.predict(vectorized_text)

            # Output the prediction
            result = {"Text": input_text, "Prediction": "Spam" if prediction[0] == 1 else "Ham"}
            return render_template('result.html', result=result)

        except Exception as e:
            return jsonify({"error": str(e)})

    # If it's a GET request, render the predict page
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)
