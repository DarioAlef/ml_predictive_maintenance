from pydantic import BaseModel, Field, validator

class InputData(BaseModel):
    """Modelo de dados para predição de falhas"""
    
    type_ordinal: int = Field(..., description="Tipo da máquina (0=L, 1=M, 2=H)", ge=0, le=2)
    air_temp: float = Field(..., description="Temperatura do ar [K]", ge=295, le=305)
    process_temp: float = Field(..., description="Temperatura do processo [K]", ge=305, le=315)
    rot_speed: float = Field(..., description="Velocidade rotacional [rpm]", ge=1000, le=3000)
    torque: float = Field(..., description="Torque [Nm]", ge=10, le=80)
    tool_wear: float = Field(..., description="Desgaste da ferramenta [min]", ge=0, le=250)
    
    @validator('type_ordinal')
    def validate_type(cls, v):
        if v not in [0, 1, 2]:
            raise ValueError('type_ordinal deve ser 0 (L), 1 (M) ou 2 (H)')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "type_ordinal": 1,
                "air_temp": 300.0,
                "process_temp": 310.0,
                "rot_speed": 1500.0,
                "torque": 40.0,
                "tool_wear": 100.0
            }
        }