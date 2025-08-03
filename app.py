import streamlit as st
import requests
import json
import os

st.title("🔧 Predictive Maintenance - Failure Type Classifier")

# Input fields
udi = st.number_input("UDI", min_value=1, step=1)
product_id = st.text_input("Product ID", value="L47181")
type_ = st.selectbox("Machine Type", ["L", "M", "H"])
air_temp = st.number_input("Air Temperature [K]", value=298.2)
process_temp = st.number_input("Process Temperature [K]", value=308.6)
rpm = st.number_input("Rotational Speed [rpm]", value=1400)
torque = st.number_input("Torque [Nm]", value=45.0)
tool_wear = st.number_input("Tool Wear [min]", value=5)
target = st.selectbox("Target (1 = Failure, 0 = Normal)", [0, 1])

if st.button("Predict Failure Type"):
    payload = {
        "input_data": [
            {
                "fields": [
                    "UDI", "Product ID", "Type",
                    "Air temperature [K]", "Process temperature [K]",
                    "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]", "Target"
                ],
                "values": [[udi, product_id, type_, air_temp, process_temp, rpm, torque, tool_wear, target]]
            }
        ]
    }

    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")

    token_response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    access_token = token_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        prediction = result['predictions'][0]['values'][0][0]
        st.success(f"🔍 Predicted Failure Type: **{prediction}**")
    else:
        st.error(f"API Error: {response.status_code} — {response.text}")
