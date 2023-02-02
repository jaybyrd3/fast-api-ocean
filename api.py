import uvicorn
import json
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "PISS OFF"


@app.get("/get_steam")
def get_steam(id):
    url = "https://steamcommunity.com/market/itemordershistogram"
    params = {"country": "US", "currency": 1,"language": "english", "item_nameid": id,"two_factor": 0}
    r = requests.get(url=url, params=params)
    return(r.json())


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
