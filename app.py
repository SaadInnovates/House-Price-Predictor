import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor

# Load CatBoost model
@st.cache_resource
def load_model():
    model = CatBoostRegressor()
    model.load_model("catboost_final_model.cbm")
    return model

model = load_model()

# App Title
st.title("🏘️ Real Estate Price Predictor")

# User Inputs
st.subheader("Enter Property Details")

city = st.selectbox("City", ["Lahore", "Karachi", "Islamabad", "Other"])
area = st.text_input("Area (e.g., DHA Phase 6)")
location = st.text_input("Location (e.g., DHA Defence)")

bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
baths = st.number_input("Number of Bathrooms", min_value=0, step=1)
size = st.number_input("Size of Property", min_value=0, step=50, help="Unit unknown (possibly in sqft or marla)")

if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "city": city,
        "area": area,
        "location": location,
        "bedrooms": bedrooms,
        "baths": baths,
        "size": size
    }])

    # Prediction
    predicted_price = model.predict(input_data)[0]
    st.success(f"🏷️ Estimated Property Price: PKR {predicted_price:,.0f}")
