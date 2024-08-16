import pandas as pd
import numpy as np


def clean_csv(csv_path):
    print(f"Cleaning CSV file: {csv_path}")

    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Example cleaning steps
    df.replace("?", np.nan, inplace=True)  # Replace '?' with NaN
    df.dropna(inplace=True)  # Remove rows with missing values
    df.drop_duplicates(inplace=True)  # Remove duplicate rows
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]  # Standardize column names

    cleaned_csv_path = csv_path.replace('.csv', '_cleaned.csv')
    df.to_csv(cleaned_csv_path, index=False)

    print(f"CSV file cleaned and saved as: {cleaned_csv_path}")
    return cleaned_csv_path


def generate_csv_summary(csv_path):
    df = pd.read_csv(csv_path)
    summary = df.describe(include='all')
    return summary
