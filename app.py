from flask import Flask, render_template, request
import pickle
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load trained model
with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Read inputs
            temperature = float(request.form["temperature"])
            occupants = int(request.form["occupants"])
            has_ac = 1 if request.form["has_ac"] == "Yes" else 0
            date = datetime.strptime(request.form["date"], "%Y-%m-%d")
            peak_usage = 0 if has_ac == 0 else max(0, temperature - 20) * 0.5


            # Extract date features
            day = date.day
            month = date.month
            weekday = date.weekday()

            # ⚠️ Correct feature order exactly as in training
            input_df = pd.DataFrame([[
                occupants,       # Household_Size
                temperature,     # Avg_Temperature_C
                has_ac,          # Has_AC
                0,               # Peak_Hours_Usage_kWh (default)
                day,
                month,
                weekday
            ]], columns=[
                "Household_Size",
                "Avg_Temperature_C",
                "Has_AC",
                "Peak_Hours_Usage_kWh",
                "day",
                "month",
                "weekday"
            ])

            # Make prediction
            prediction = round(model.predict(input_df)[0], 2)

        except Exception as e:
            error = f"Error: {e}"

    return render_template("index.html", prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(debug=True)
