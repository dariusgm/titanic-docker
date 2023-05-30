import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, request, jsonify

# Download the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
dataset = pd.read_csv(url)

# Perform data splitting
X = dataset.drop("Survived", axis=1)
y = dataset["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform feature engineering
# For simplicity, let's assume we're dropping some irrelevant columns and encoding categorical variables

# Drop irrelevant columns
X_train = X_train.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
X_test = X_test.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)

# Encode categorical variables
X_train = pd.get_dummies(X_train, columns=["Sex", "Embarked"])
X_test = pd.get_dummies(X_test, columns=["Sex", "Embarked"])

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Create a Flask API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    passenger_data = pd.DataFrame(data)
    passenger_data = passenger_data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1)
    passenger_data = pd.get_dummies(passenger_data, columns=["Sex", "Embarked"])
    prediction = model.predict(passenger_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run()

