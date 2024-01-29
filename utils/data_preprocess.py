# In this script put all the code from your notebook that does all the text cleaning and vectorization
# write them in modules in such a way that each module takes 1 string of text performs the cleaning as you have done in the notebook(preprocess, stemmer and the vectorization part)


import pandas as pd
import spacy
from nltk.stem import PorterStemmer
from spacy.lang.en.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils import resample

nlp = spacy.load('en_core_web_sm')

def preprocess(text):
    doc = nlp(text)
    no_stop_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(no_stop_words)

def stemmer(text):
    text = text.split()
    words = ''
    stemmer = PorterStemmer()
    for i in text:
        words += (stemmer.stem(i)) + ' '
    return words.strip()

def vectorize_text(data):
    v = CountVectorizer(ngram_range=(1, 3))
    vectorized_data = v.fit_transform(data)
    return v, vectorized_data

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    Spam_upsampling = resample(df[df.Category == 'spam'], n_samples=len(df[df.Category == 'ham']), replace=True)
    ham = df[df.Category == 'ham']
    df_new = pd.concat([Spam_upsampling, ham])
    df_new['Spam'] = df.Category.apply(lambda x: 1 if x == 'spam' else 0)
    df_new['Message_new'] = df_new.Message.apply(preprocess)
    df_new['Message_Stemmed'] = df_new.Message_new.apply(stemmer)
    return df_new
