import uvicorn
from fastapi import FastAPI

from app.api.v1 import players, rooms

app = FastAPI()

app.include_router(players.router, prefix="/api/v1")
app.include_router(rooms.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
