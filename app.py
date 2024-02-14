from flask import Flask, render_template, request, jsonify
import spacy
from nltk.stem import PorterStemmer
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from utils.data_preprocess import preprocess, stemmer
from utils.model_pipeline import model, vectorizer

app = Flask(__name__)


# Load spaCy for text processing
nlp = spacy.load("en_core_web_sm")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Get the input text from the form
            input_text = request.form["text"]

            # Preprocess and stem the input text
            processed_text = preprocess(input_text)
            stemmed_text = stemmer(processed_text)

            # Vectorize the input text using the CountVectorizer fitted on the training data
            vectorized_text = vectorizer.transform([stemmed_text])

            # Make prediction
            prediction = model.predict(vectorized_text)

            # Output the prediction
            result = {
                "Text": input_text,
                "Prediction": "Spam" if prediction[0] == 1 else "Ham",
            }
            return render_template("result.html", result=result)

        except Exception as e:
            return jsonify({"error": str(e)})

    # If it's a GET request, render the predict page
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
