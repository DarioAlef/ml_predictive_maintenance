import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.backend.application.api.router import router as v1_router  # ✅ Mudou!

app = FastAPI(
    title="API de Manutenção Preditiva",
    description="Predição de falhas em máquinas de usinagem",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api", tags=["Predição"])

@app.get("/")
async def root():
    return {"message": "API de Manutenção Preditiva está rodando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "app.backend.main:app",  # ✅ Mudou!
        host="0.0.0.0",
        port=5000,
        reload=True
    )