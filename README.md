# 🏘️ Real Estate Price Predictor

A machine learning-powered Streamlit web app that predicts real estate property prices in major Pakistani cities using a trained CatBoost regression model. The app supports input in both **square feet** and **marlas**, with real-time price estimation based on location, size, and other property features.

---

## 📌 Features

- Supports multiple cities: Lahore, Karachi, Islamabad, Multan, Faisalabad, and more
- Input flexibility: Size can be entered in marlas or square feet
- Fast, accurate predictions using a trained CatBoost model
- Clean and responsive user interface (built with Streamlit)

---

## 📊 Model Performance

| Metric        | Value       |
|---------------|-------------|
| Algorithm     | CatBoostRegressor |
| Feature Set   | `['city', 'area', 'location', 'bedrooms', 'baths', 'size']` |
| Target        | Log-transformed `price` |
| Evaluation Metric | RMSE |
| Validation R² | **0.91+** |
| Training R²   | **0.87** |
| Regularization | Early stopping, L2 leaf reg, bagging temperature |

> ⚠️ Model was trained on cleaned, structured real estate data, mostly from major urban areas in Pakistan. Predictions for less common localities may vary in accuracy.

---

## 🛠️ Tech Stack

| Layer         | Technology        |
|---------------|-------------------|
| Model       | CatBoost Regressor |
| Data Prep   | Pandas, NumPy     |
| Interface   | Streamlit         |
| Deployment  | Streamlit Cloud / Local |
| Format      | `.cbm` (CatBoost binary model) |
| Language     | Python 3.9+       |

---


