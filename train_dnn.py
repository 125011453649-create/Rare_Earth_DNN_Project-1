
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load prepared dataset
df = pd.read_csv("dataset/model_ready_data.csv")

target = "Total_REE_ppm"
features = [col for col in df.columns if col != target]

X = df[features]
y = df[target]

# 2. Check dataset
print("Samples:", len(df))
print("Features:", len(features))

# 3. Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 4. Scale input features
x_scaler = StandardScaler()

X_train_scaled = x_scaler.fit_transform(X_train)
X_test_scaled = x_scaler.transform(X_test)

# 5. Transform target values
y_train_log = np.log1p(y_train.values).reshape(-1, 1)

y_scaler = StandardScaler()
y_train_scaled = y_scaler.fit_transform(
    y_train_log
).ravel()

# 6. Create Deep Neural Network
model = MLPRegressor(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    alpha=1.0,
    learning_rate_init=0.001,
    max_iter=3000,
    random_state=42
)

# 7. Train model
print("\nTraining DNN model...")

model.fit(X_train_scaled, y_train_scaled)

# 8. Make predictions
pred_scaled = model.predict(X_test_scaled)

pred_log = y_scaler.inverse_transform(
    pred_scaled.reshape(-1, 1)
).ravel()

predictions = np.expm1(pred_log)

# 9. Evaluate model
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nDNN MODEL RESULTS")
print("-----------------------")
print("MAE:", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

# 10. Compare with simple baseline
baseline = DummyRegressor(strategy="median")
baseline.fit(X_train, y_train)
baseline_pred = baseline.predict(X_test)

baseline_mae = mean_absolute_error(
    y_test, baseline_pred
)

print("\nBaseline MAE:", round(baseline_mae, 2))

# 11. Save trained model and scalers
joblib.dump(
    {
        "model": model,
        "x_scaler": x_scaler,
        "y_scaler": y_scaler,
        "features": features
    },
    "model/rare_earth_dnn.pkl"
)

print("\nModel saved successfully!")
print("Location: model/rare_earth_dnn.pkl")
