import pandas as pd
import os

input_path = "data/processed/cleaned_energy.csv"
output_path = "data/processed/final_energy.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError("Run data_preprocessing.py first")

df = pd.read_csv(input_path)

# Convert Date column to datetime AGAIN (CSV does not preserve dtype)
df['Date'] = pd.to_datetime(df['Date'], errors='raise')

df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month
df['weekday'] = df['Date'].dt.weekday

df.drop(columns=['Date'], inplace=True)

df.to_csv(output_path, index=False)

print("Feature engineering completed successfully")
