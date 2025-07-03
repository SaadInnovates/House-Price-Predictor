# 🏘️ Real Estate Price Predictor

A machine learning-powered Streamlit web app that predicts real estate property prices in major Pakistani cities using a trained CatBoost regression model. The app supports input in both **square feet** and **marlas**, with real-time price estimation based on city, area, and property features.
Check out the live app here: [🏡 Real Estate Price Predictor](https://house-price-predictor-by-saad.streamlit.app/)

---

## 📌 Features

- Supports multiple cities: **Lahore, Karachi, Islamabad, Multan, Faisalabad, Peshawar, Quetta, Rawalpindi, Murree, Gujranwala, Attock, 2_FECHS**, and others
- Input flexibility: Size can be entered in **marlas** or **square feet**
- Real-time price prediction using a tuned **CatBoost** model
- Log-transformed target variable for better modeling of skewed price data
- Clean, responsive UI built with **Streamlit**
- Efficient performance on both local and cloud deployment

---

## 🧠 Model Performance

| Metric           | Value                    |
|------------------|--------------------------|
| Algorithm        | CatBoostRegressor        |
| Hyperparameter Tuning | Optuna (10 Trials)       |
| Feature Set      | `['city', 'area', 'location', 'bedrooms', 'baths', 'size']` |
| Target Variable  | Log-transformed `price`  |
| Mean CV R² Score | **0.8446**               |
| Best Fold R²     | **0.8897**               |
| Train R² Score   | **0.87**                 |

> ✅ The model was validated using 5-fold cross-validation and shows **strong generalization** across urban datasets.

> ⚠ Model performance may decrease slightly on underrepresented or rural areas.

---

## 🛠️ Tech Stack

| Layer         | Technology          |
|---------------|---------------------|
| Machine Learning | CatBoost Regressor |
| Data Processing  | Pandas, NumPy       |
| Frontend         | Streamlit           |
| Deployment       | Streamlit Cloud / Local |
| Model Format     | `.cbm` (CatBoost binary) |
| Language         | Python 3.9+         |

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/real-estate-price-predictor.git
cd real-estate-price-predictor

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
