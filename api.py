import uvicorn
import json
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "PISS OFF"


@app.get("/get_link")
def get_link(link):
    r = requests.get(link)
    return(r.json())


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
