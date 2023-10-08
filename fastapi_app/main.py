"""Main fastapi configuration"""

from fastapi import FastAPI

from .api.v1.router import router as v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])

if __name__ == '__main__':
    raise RuntimeError("Run the fastapi_app by using 'python -m fastapi_app'")