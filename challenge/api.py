import fastapi
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from challenge.model import DelayModel
import pandas as pd


app = fastapi.FastAPI()

model=DelayModel()
data = pd.read_csv('data/data.csv')
features, target = model.preprocess(data=data,target_column="delay")
model.fit(features=features,target=target)

flights_by_airline = data['OPERA'].value_counts()
op=flights_by_airline.index.values
mes=[1,2,3,4,5,6,7,8,9,10,11,12]
tipo=["N","I"]
"""
    OPERA: str
    MES: int
    TIPOVUELO: str
"""

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }


@app.post("/predict", status_code=200)
async def post_predict(dic: dict) -> dict:
    dic=dic["flights"][0]
    if dic["OPERA"] not in op:
        raise HTTPException(status_code=400, detail="Invalid 'OPERA' value.")
    if dic["MES"] not in mes:
        raise HTTPException(status_code=400, detail="Invalid 'MES' value.")
    if dic["TIPOVUELO"] not in tipo:
        raise HTTPException(status_code=400, detail="Invalid 'TIPOVUELO' value.")

    df_data = pd.DataFrame({
        "OPERA_"+dic["OPERA"]:1,
        "MES_"+str(dic["MES"]):1,
        "TIPOVUELO_"+dic["TIPOVUELO"]:1
    },index=[0])
    for column in features.columns:
        if column not in df_data.columns:
            df_data[column]=0
    
    for column in df_data.columns:
        if column not in features.columns:
            df_data.drop(column,axis=1,inplace=True)

    pred=model.predict(df_data)

    response={
        "predict": pred
    }


    return JSONResponse(content=response)

