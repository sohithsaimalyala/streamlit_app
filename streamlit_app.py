import streamlit as st
import requests

# Define the FastAPI endpoint (replace with your deployed model URL)
API_ENDPOINT = "https://housing-prediction-flif.onrender.com/predict"

# App title and description
st.title("Real-Time Classification with FastAPI Model")
st.write("This app allows you to interact with the deployed FastAPI model for real-time predictions.")

# Sidebar inputs
st.sidebar.header("Input Features")
size = st.sidebar.number_input("Property Size (Square Footage)", min_value=100.0, max_value=10000.0, value=1000.0)
rooms = st.sidebar.number_input("Number of Rooms", min_value=1, max_value=20, value=3)
location = st.sidebar.selectbox("Location Type", ["Urban", "Suburban", "Rural"])

# Create input payload for the API
input_data = {
    "size": size,
    "rooms": rooms,
    "location": location
}

# Display input data
st.subheader("Your Input Data")
st.json(input_data)

# Button to get the prediction
if st.button("Get Prediction"):
    try:
        # Make a POST request to the API
        response = requests.post(API_ENDPOINT, json=input_data)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse the response
        prediction = response.json()
        st.success(f"Prediction: {prediction.get('prediction', 'Unknown')}")
        st.write("Details:", prediction)

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to API: {e}")
