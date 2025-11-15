import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
rfc = joblib.load('model.joblib')

st.title("Machine Predictive Maintenance Classification")

# Mapping
type_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

# UI layout
col1, col2 = st.columns(2)

with col1:
    selected_type = st.selectbox('Select a Type', ['Low', 'Medium', 'High'])
    selected_type = type_mapping[selected_type]

with col2:
    air_temperature = st.number_input('Air temperature [K]', value=300.0)

with col1:
    process_temperature = st.number_input('Process temperature [K]', value=310.0)

with col2:
    rotational_speed = st.number_input('Rotational speed [rpm]', value=1500.0)

with col1:
    torque = st.number_input('Torque [Nm]', value=40.0)

with col2:
    tool_wear = st.number_input('Tool wear [min]', value=10.0)

# Prediction
if st.button('Predict Failure'):

    try:
        # Create DataFrame with correct column names
        input_df = pd.DataFrame([{
            'Type': selected_type,
            'Air temperature [K]': air_temperature,
            'Process temperature [K]': process_temperature,
            'Rotational speed [rpm]': rotational_speed,
            'Torque [Nm]': torque,
            'Tool wear [min]': tool_wear
        }])

        prediction = rfc.predict(input_df)

        if prediction[0] == 1:
            st.success('⚠️ Failure Detected!')
        else:
            st.success('✅ No Failure')

    except Exception as e:
        st.error(f"Error: {e}")
