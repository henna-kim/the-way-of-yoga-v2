from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import offer, index, yoga_poses

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(offer.router)
app.include_router(index.router)
app.include_router(yoga_poses.router)
