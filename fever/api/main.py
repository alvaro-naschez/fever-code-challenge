from fastapi import FastAPI

from .v1 import api_router

app = FastAPI()
app.include_router(api_router)
