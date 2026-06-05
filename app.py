# Import required libraries
import streamlit as st
import pandas as pd
import joblib

# Load model and feature names
model = joblib.load("churn_model.pkl")
feature_names = joblib.load("feature_names.pkl")

# Dashboard title
st.title("Customer Churn Intelligence System")

st.write("Predict whether a customer is likely to churn.")

# User inputs
tenure = st.number_input("Tenure (Months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

# Prediction button
if st.button("Predict Churn"):

    # Create sample input row
    input_data = pd.DataFrame([[0]*len(feature_names)], columns=feature_names)

    # Fill available features if they exist
    if 'tenure' in input_data.columns:
        input_data['tenure'] = tenure

    if 'MonthlyCharges' in input_data.columns:
        input_data['MonthlyCharges'] = monthly_charges

    if 'TotalCharges' in input_data.columns:
        input_data['TotalCharges'] = total_charges

    # Make prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer Likely To Churn")
    else:
        st.success("Customer Likely To Stay")