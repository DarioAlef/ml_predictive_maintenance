from fastapi import APIRouter
from app.backend.application.api.endpoint.predict_failure import router as predict_failure_router


router = APIRouter()

router.include_router(predict_failure_router)