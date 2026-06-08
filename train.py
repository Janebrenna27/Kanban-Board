from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib

data = load_iris()

model = RandomForestClassifier()
model.fit(data.data, data.target)

joblib.dump(model, "model.pkl")

print("Model Trained")