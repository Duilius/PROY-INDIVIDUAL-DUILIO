from fastapi import FastAPI
from router.sucursales import carga

app=FastAPI()

app.include_router(carga)