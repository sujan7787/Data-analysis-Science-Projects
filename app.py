import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the best model and scaler
model = joblib.load('best_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title('ER Visit Chance Prediction')
st.write('Enter patient details to predict the chance of an ER visit.')

# Input fields for features
age = st.slider('Age', 60, 100, 75)
heart_rate = st.slider('Heart Rate', 80, 140, 110)
resp_rate = st.slider('Respiratory Rate', 20, 35, 27)
oxygen_sat = st.slider('Oxygen Saturation (%)', 80, 100, 90)
temperature = st.slider('Temperature (°F)', 96.0, 102.0, 98.6)
dry_cough = st.checkbox('Dry Cough (1 for Yes, 0 for No)')
dry_cough_val = 1 if dry_cough else 0
days_since_discharge = st.slider('Days Since Discharge', 1, 7, 3)

# Create a DataFrame from user inputs
input_data = pd.DataFrame([[age, heart_rate, resp_rate, oxygen_sat, temperature, dry_cough_val, days_since_discharge]],
                            columns=['age', 'heart_rate', 'resp_rate', 'oxygen_sat', 'temperature', 'dry_cough', 'days_since_discharge'])

# Scale the input data
scaled_input = scaler.transform(input_data)

# Make prediction
prediction = model.predict(scaled_input)[0]

st.subheader('Prediction Result:')
st.write(f'The predicted chance of an ER visit is: {prediction:.2f}')
