import streamlit as st
import requests
import pandas as pd

# API endpoint
API_URL = 'http://localhost:5000/predict'

# Streamlit app
st.title('Titanic Survival Prediction')

# Collect passenger data
pclass = st.selectbox('Passenger Class', [1, 2, 3])
sex = st.selectbox('Sex', ['male', 'female'])
age = st.number_input('Age')
sib_sp = st.number_input('Siblings/Spouses Aboard', min_value=0)
par_ch = st.number_input('Parents/Children Aboard', min_value=0)
fare = st.number_input('Fare')
embarked = st.selectbox('Embarked', ['C', 'Q', 'S'])

# Prepare payload
data = {
    'Pclass': pclass,
    'Sex': sex,
    'Age': age,
    'SibSp': sib_sp,
    'Parch': par_ch,
    'Fare': fare,
    'Embarked': embarked
}

# Make prediction request
if st.button('Predict'):
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.success(f"The predicted survival outcome is {prediction}")
    else:
        st.error('Prediction failed. Please try again.')

# Display dataset
st.header('Passenger Data')
df = pd.DataFrame(data, index=[0])
st.table(df)


