import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model pipeline
pipeline = joblib.load('random_forest_credit_model.joblib')

# Load the original data to dynamically get column names and options for the input form
original_data = pd.read_csv("german_credit_data.csv")
categorical_features = original_data.select_dtypes(include=['object']).columns.tolist()
numerical_features = original_data.select_dtypes(exclude=['object']).columns.tolist()

st.title("Credit Scoring using Random Forest")
st.write("Enter the attributes below to predict the creditworthiness.")

# Create input widgets for all attributes, dynamically
input_data = {}
for col in original_data.columns:
    if col == 'class':
        continue
    
    if col in categorical_features:
        # Use unique values from the original data as options
        options = original_data[col].unique().tolist()
        input_data[col] = st.selectbox(f"Select {col}", options)
    elif col in numerical_features:
        # Use a number input for numerical columns
        input_data[col] = st.number_input(f"Enter {col}", value=float(original_data[col].mean()))

# Create a DataFrame from the user input
input_df = pd.DataFrame([input_data])

if st.button("Predict Credit Score"):
    # The pipeline's preprocessor automatically transforms the input_df
    # to the format the model expects, handling the one-hot encoding internally.
    try:
        prediction = pipeline.predict(input_df)

        if prediction[0] == 1:
            st.success("The model predicts a **Good** credit risk.")
        else:
            st.error("The model predicts a **Bad** credit risk.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")