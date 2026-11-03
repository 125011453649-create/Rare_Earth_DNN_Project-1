
import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Rare Earth Prediction",
    page_icon="🌍"
)

st.title("🌍 Rare Earth Mineral Prediction")
st.write("DNN-Based Geological Concentration Prediction")

# Load trained model
data = joblib.load("model/rare_earth_dnn.pkl")

model = data["model"]
x_scaler = data["x_scaler"]
y_scaler = data["y_scaler"]
features = data["features"]

st.subheader("Enter Geological Parameters")

values = {}

for feature in features:
    values[feature] = st.number_input(
        feature,
        value=0.0,
        format="%.4f"
    )

if st.button("Predict Total REE"):
    input_df = pd.DataFrame([values])

    scaled_input = x_scaler.transform(input_df)

    prediction_scaled = model.predict(scaled_input)

    prediction_log = y_scaler.inverse_transform(
        prediction_scaled.reshape(-1, 1)
    )

    prediction = np.expm1(prediction_log[0][0])

    st.success("Prediction Completed!")

    st.metric(
        "Predicted Total REE",
        f"{prediction:.2f} ppm"
    )

    st.info(
        "Research prototype result. "
        "Validate with laboratory measurements."
    )
