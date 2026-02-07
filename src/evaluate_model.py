import pandas as pd
import pickle
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("data/processed/final_energy.csv")

X = df.drop('Energy_Consumption_kWh', axis=1)
y = df['Energy_Consumption_kWh']

with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

predictions = model.predict(X)

mae = mean_absolute_error(y, predictions)
r2 = r2_score(y, predictions)

with open("results/metrics.txt", "w") as f:
    f.write(f"MAE: {mae}\n")
    f.write(f"R2 Score: {r2}\n")

print("MAE:", mae)
print("R2 Score:", r2)
