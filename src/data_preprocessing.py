import pandas as pd
import os

input_path = "data/raw/energy.csv"
output_path = "data/processed/cleaned_energy.csv"

df = pd.read_csv(input_path)

# Clean column names
df.columns = df.columns.str.strip()

# Convert date (auto-detect format)
df['Date'] = pd.to_datetime(df['Date'], errors='raise')

# Encode categorical column
df['Has_AC'] = df['Has_AC'].map({'Yes': 1, 'No': 0})

# Drop Household_ID
df.drop(columns=['Household_ID'], inplace=True)

os.makedirs("data/processed", exist_ok=True)
df.to_csv(output_path, index=False)

print("Data preprocessing completed successfully")
