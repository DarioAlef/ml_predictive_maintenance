from fastapi import APIRouter
from app.backend.application.schemas.input_data_model import InputData
from app.backend.application.model_loader import model
import pandas as pd

router = APIRouter()

# ✅ Valores médios e desvios padrão do StandardScaler
SCALER_MEAN = {
    'Air temperature [K]': 300.004,
    'Process temperature [K]': 310.005,
    'Rotational speed [rpm]': 1538.776,
    'Torque [Nm]': 39.987,
    'Tool wear [min]': 107.951,
    'Type_ordinal': 1.0
}

SCALER_STD = {
    'Air temperature [K]': 2.000,
    'Process temperature [K]': 1.483,
    'Rotational speed [rpm]': 179.284,
    'Torque [Nm]': 9.968,
    'Tool wear [min]': 63.654,
    'Type_ordinal': 0.816
}

@router.post("/predict_failure")
def predict(data: InputData):
    """Predição de falha em máquina de usinagem"""
    
    # ✅ Garantir que type_ordinal seja inteiro
    type_ord = int(data.type_ordinal)
    
    print(f"\n{'='*50}")
    print(f"🔹 Dados recebidos:")
    print(f"  Type: {type_ord} (tipo: {type(type_ord).__name__})")
    print(f"  Air Temp: {data.air_temp} K")
    print(f"  Process Temp: {data.process_temp} K")
    print(f"  Rot Speed: {data.rot_speed} rpm")
    print(f"  Torque: {data.torque} Nm")
    print(f"  Tool Wear: {data.tool_wear} min")
    print(f"{'='*50}\n")
    
    # 1️⃣ Criar DataFrame com valores BRUTOS (na ordem EXATA do treinamento)
    features_raw = pd.DataFrame({
        'Air temperature [K]': [float(data.air_temp)],
        'Process temperature [K]': [float(data.process_temp)],
        'Rotational speed [rpm]': [float(data.rot_speed)],
        'Torque [Nm]': [float(data.torque)],
        'Tool wear [min]': [float(data.tool_wear)],
        'Type_ordinal': [float(type_ord)]  # ✅ Convertido para float após validação
    })
    
    # 2️⃣ NORMALIZAR os dados (Z-score)
    features_normalized = features_raw.copy()
    for col in features_raw.columns:
        features_normalized[col] = (features_raw[col] - SCALER_MEAN[col]) / SCALER_STD[col]
    
    print("📋 Features BRUTAS:")
    print(features_raw)
    print("\n📊 Features NORMALIZADAS:")
    print(features_normalized)
    print(f"Shape: {features_normalized.shape}\n")
    
    try:
        # 3️⃣ Predição
        proba = model.predict_proba(features_normalized)[:, 1][0]
        prediction = 1 if proba >= 0.5 else 0

        print(f"✅ Resultado:")
        print(f"  Probabilidade: {proba*100:.2f}%")
        print(f"  Predição: {'FALHA' if prediction == 1 else 'NORMAL'}")
        print(f"{'='*50}\n")

        return {
            "probability": float(proba),
            "prediction": int(prediction),
            "risk_level": "Alto" if prediction == 1 else "Baixo",
            "confidence": f"{proba * 100:.1f}%"
        }
    except Exception as e:
        print(f"❌ ERRO: {str(e)}")
        raise