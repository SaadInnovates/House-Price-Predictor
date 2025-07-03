import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor, Pool

# ------------------------------
# Load the CatBoost model
# ------------------------------
@st.cache_resource
def load_model():
    model = CatBoostRegressor()
    model.load_model("catboost_final_model.cbm")
    return model

model = load_model()

# ------------------------------
# UI Layout
# ------------------------------
st.title("🏘️ Real Estate Price Predictor")
st.markdown("Enter the property details below to estimate the property price in PKR.")

# Expanded list of cities
cities = [
    'Lahore', 'Karachi', 'Islamabad', 'Multan', 'Faisalabad',
    'Peshawar', 'Quetta', 'Rawalpindi', 'Murree', 'Gujranwala',
    'Attock', '2_FECHS', 'Bahawalpur', 'Sargodha', 'Sialkot',
    'Hyderabad', 'Abbottabad', 'Jhelum', 'Okara', 'Other'
]

# Inputs
city = st.selectbox("City", cities)
area = st.text_input("Area (e.g., DHA Phase 6)")
location = st.text_input("Location (e.g., DHA Defence)")
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
baths = st.number_input("Number of Bathrooms", min_value=0, step=1)

# Size input choice
size_unit = st.radio("How would you like to enter the property size?", ["Square Feet", "Marlas"])

if size_unit == "Square Feet":
    size = st.number_input("Size (in square feet)", min_value=0, step=50)
else:
    marlas = st.number_input("Size (in marlas)", min_value=0.0, step=0.5)
    size = marlas * 272.25
    st.markdown(f"📐 Converted Size: **{size:,.0f} sq. feet**")

# Predict button
if st.button("Predict Price"):
    # Create input DataFrame
    input_data = pd.DataFrame([{
        "city": city,
        "area": area,
        "location": location,
        "bedrooms": bedrooms,
        "baths": baths,
        "size": size
    }])

    # Set categorical columns as category dtype
    cat_features = ['city', 'area', 'location']
    for col in cat_features:
        input_data[col] = input_data[col].astype("category")

    # Create Pool for prediction
    input_pool = Pool(data=input_data, cat_features=cat_features)

    # Predict log price
    predicted_log_price = model.predict(input_pool)[0]

    # Reverse log1p transform
    predicted_price = np.expm1(predicted_log_price)

    # Show result
    st.success(f"🏷️ Estimated Property Price: PKR {predicted_price:,.0f}")
