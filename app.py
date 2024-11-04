from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Provide the absolute path to the file
model_file_path = r'C:\Users\rohan\OneDrive\Desktop\data science\capstone projects\spam detection/spamclassifier_MnB.pkl'
vectorizer_file_path = r'C:\Users\rohan\OneDrive\Desktop\data science\capstone projects\spam detection/vectorizer.pkl'

# Load the model
with open(model_file_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load the vectorizer
with open(vectorizer_file_path, 'rb') as vectorizer_file:
    vect = pickle.load(vectorizer_file)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            msg = str(request.form['mesg'])
            transformed = vect.transform([msg])
            trans_data = transformed.toarray()
            pred = model.predict(trans_data)
            output = str(pred[0])
            return render_template('result.html', prediction=f'{output}')
    except Exception as e:
        return render_template('result.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
