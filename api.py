import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify

# Download the Titanic dataset
url = "data/titanic.csv"
dataset = pd.read_csv(url) \
    .drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1) \
    .dropna()

# Perform data splitting
X = pd\
    .get_dummies(dataset, columns=["Sex", "Embarked"])\
    .drop("Survived", axis=1)
y = dataset["Survived"]
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

# extract all columns and fill them with 0 at predict time
columns = dataset.columns

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    print(data)
    passenger_data = pd.DataFrame([data])
    passenger_data = pd.get_dummies(passenger_data, columns=["Sex", "Embarked"])

    prediction = model.predict(passenger_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run()

