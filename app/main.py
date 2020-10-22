from fastapi import FastAPI

from api.metar import view as metar

app = FastAPI()

FBW_WELCOME_MSG = "FlyByWire Simulations API v1.0"

@app.get("/")
def read_root():
    return FBW_WELCOME_MSG

app.include_router(metar.router, prefix="/metar")