import joblib

model = joblib.load("model.pkl")

pred = model.predict([[5]])
print("Prediction:", pred[0])
