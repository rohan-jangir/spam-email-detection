# Spam Detection Flask Application

This repository contains a Flask application that utilizes a machine learning model to classify text messages as spam or not spam. The application is designed to be simple and user-friendly, allowing users to input messages and receive immediate predictions.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Model Training](#model-training)
- [License](#license)
- [Contributing](#contributing)

## Technologies Used

- Python
- Flask
- NumPy
- scikit-learn
- Pickle
- HTML/CSS (for the frontend)

## Install the required packages:
```bash
pip install Flask numpy scikit-learn
```
**Note:** Place your model and vectorizer files in the appropriate directory: Ensure that your model file (spamclassifier_MnB.pkl) and vectorizer file (vectorizer.pkl) are located in the spam detection directory within your project. Update the paths in the code if necessary.

## Model Training
The model is trained using a dataset of messages labeled as spam or not spam. It utilizes a Multinomial Naive Bayes classifier. If you wish to retrain the model, ensure you have the necessary dataset and update the training code accordingly.
