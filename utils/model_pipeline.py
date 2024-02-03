# Modules in this script will be loading your ML models from the 'model' folder, using this pretrained model to do the prediction based on the input text and send the classification output
# from your notebook, save the trained model as a .pkl pickle file and put it inside the 'model' folder. Define a function that loads this pickle file and returns it which basically acts as the object using which you can do .predict()
# you will be importing the functions from data_preprocess file to do the cleaning/transformation and return the classification output.
# Load your saved model
import pickle

with open("models/model_pickle", "rb") as f:
    model = pickle.load(f)

# Load the vectorizer
with open("models/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
