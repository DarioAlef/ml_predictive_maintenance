import pandas as pd
from pathlib import Path

# Carregar x_train para ver as colunas
base_path = Path("data/processed")
x_train = pd.read_csv(base_path / "x_train.csv")

print("Colunas do x_train (ordem correta):")
print(x_train.columns.tolist())
print(f"\nTotal de colunas: {len(x_train.columns)}")
print("\nPrimeiras linhas:")
print(x_train.head())