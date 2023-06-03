import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify

# Download the Titanic dataset
path = "data/titanic.csv"
target = "Survived"
dataset = pd.read_csv(path) \
    .drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1) \
    .dropna()

# Perform data splitting
X = pd\
    .get_dummies(dataset, columns=["Sex", "Embarked"])\
    .drop(target, axis=1)
y = dataset[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Create a Flask API
app = Flask(__name__)

features = list(X.columns)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    vector = {}
    for feature in features:
        if "_" in feature:
            key, value = feature.split("_")
            if key in data and value == data[key]:
                vector[f"{key}_{value}"] = 1
            else:
                vector[f"{key}_{value}"] = 0
        else:
            if feature in data:
                vector[feature] = data[feature]
            else:
                vector[feature] = 0

    passenger_data = pd.DataFrame([vector])
    prediction = model.predict(passenger_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run()

