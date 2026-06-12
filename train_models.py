from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import joblib
import os

os.makedirs("models", exist_ok=True)

# Disease Model
X, y = make_classification(
    n_samples=500,
    n_features=6,
    random_state=42
)

disease_model = RandomForestClassifier()
disease_model.fit(X, y)

joblib.dump(
    disease_model,
    "models/disease_model.pkl"
)

# Outcome Model
X2, y2 = make_classification(
    n_samples=500,
    n_features=5,
    random_state=42
)

outcome_model = RandomForestClassifier()
outcome_model.fit(X2, y2)

joblib.dump(
    outcome_model,
    "models/outcome_model.pkl"
)

print("Models created successfully")