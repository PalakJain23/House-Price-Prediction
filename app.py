import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open(r"C:\Users\mk\Desktop\House\house_model.pkl", "rb"))

# Website title
st.title("House Price Prediction")

st.write("Enter house details below")

# User inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

mainroad_yes = st.selectbox("Main Road", ["Yes", "No"])
guestroom_yes = st.selectbox("Guest Room", ["Yes", "No"])
basement_yes = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating_yes = st.selectbox("Hot Water Heating", ["Yes", "No"])
airconditioning_yes = st.selectbox("Air Conditioning", ["Yes", "No"])
prefarea_yes = st.selectbox("Preferred Area", ["Yes", "No"])

furnishing = st.selectbox(
    "Furnishing Status",
    ["Semi-Furnished", "Unfurnished"]
)

# Convert text to numbers
mainroad_yes = 1 if mainroad_yes == "Yes" else 0
guestroom_yes = 1 if guestroom_yes == "Yes" else 0
basement_yes = 1 if basement_yes == "Yes" else 0
hotwaterheating_yes = 1 if hotwaterheating_yes == "Yes" else 0
airconditioning_yes = 1 if airconditioning_yes == "Yes" else 0
prefarea_yes = 1 if prefarea_yes == "Yes" else 0

furnishingstatus_semi_furnished = 1 if furnishing == "Semi-Furnished" else 0
furnishingstatus_unfurnished = 1 if furnishing == "Unfurnished" else 0

# Prediction button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        'area': [area],
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'stories': [stories],
        'parking': [parking],
        'mainroad_yes': [mainroad_yes],
        'guestroom_yes': [guestroom_yes],
        'basement_yes': [basement_yes],
        'hotwaterheating_yes': [hotwaterheating_yes],
        'airconditioning_yes': [airconditioning_yes],
        'prefarea_yes': [prefarea_yes],
        'furnishingstatus_semi-furnished': [furnishingstatus_semi_furnished],
        'furnishingstatus_unfurnished': [furnishingstatus_unfurnished]
    })

    prediction = model.predict(input_data)

    price_lakhs = prediction[0] / 100000

    st.success(f"Predicted Price: ₹ {price_lakhs:.2f} Lakhs")