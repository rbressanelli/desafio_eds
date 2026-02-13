from fastapi import FastAPI
from app.api.v1.routes import api_router
from .core.config import settings

app = FastAPI(title="CRUD Usuários")

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
