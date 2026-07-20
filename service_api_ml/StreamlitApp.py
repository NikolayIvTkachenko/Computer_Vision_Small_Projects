import streamlit as st
import requests
from requests.exceptions import ConnectionError

ip_api = "127.0.0.1"
port_api = "5000"

st.title("Titanic Survival Prediction")
st.write("Enter the passenger details:")

pclass = st.selectbox("Ticket Class (Pclass)", [1, 2, 3])

age = st.text_input("Age", value=10)
if not age.isdigit():
    st.error("Please enter a valid number for Age.")

fare = st.text_input("Fare", value=100)
if not fare.isdigit():
    st.error("Please enter a valid number for Fare.")

if st.button("Predict"):
    if age.isdigit() and fare.isdigit():
        data = {
            "Pclass": int(pclass),
            "Age": float(age),
            "Fare": float(fare)
        }
        try:
            response = requests.post(f"http://{ip_api}:{port_api}/predict_model", json=data)

            if response.status_code == 200:
                prediction = response.json()["prediction"]
                st.success(f"Prediction: {prediction}")
            else:
                st.error(f"Request failed with status code {response.status_code}")
        except ConnectionError as e:
            st.error(f"Failed to connect to the server")
    else:
        st.error("Please fill in all fields with valid numbers")






