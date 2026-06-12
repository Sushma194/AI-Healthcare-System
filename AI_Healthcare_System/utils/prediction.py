import joblib
import numpy as np

disease_model = joblib.load(
    "models/disease_model.pkl"
)

outcome_model = joblib.load(
    "models/outcome_model.pkl"
)

def predict_disease(features):

    prediction = disease_model.predict(
        [features]
    )[0]

    probability = disease_model.predict_proba(
        [features]
    )[0][1]

    return prediction, probability


def predict_outcome(features):

    prediction = outcome_model.predict(
        [features]
    )[0]

    probability = outcome_model.predict_proba(
        [features]
    )[0][1]

    return prediction, probability