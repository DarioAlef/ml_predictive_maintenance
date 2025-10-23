import joblib
from pathlib import Path

# ✅ Caminho relativo (funciona em qualquer ambiente)
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent / "data" / "models"
MODEL_PATH = BASE_DIR / "random_forest_model.jb"

print(f"Carregando modelo de: {MODEL_PATH}")
model = joblib.load(MODEL_PATH)
print("Modelo carregado com sucesso!")

# ❌ NÃO PRECISA DE SCALER
# scaler = joblib.load(BASE_DIR / "scaler.pkl")