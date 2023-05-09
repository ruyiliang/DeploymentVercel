from fastapi import FastAPI 
import pandas as pd 

df = pd.read_csv('./data/rxsummary2018.csv')

app = FastAPI()

@app.get('/')
async def root():
    return {'This is a API service for MN Prescription Drug Summary 2018.'}

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.get("/rx/{value}")
async def rx(value):
    print('value: ', value)
    filtered = df[df['NUMBER_SCRIPTS'] == value]
    if len(filtered) <= 0:
        return {'There is nothing here.'}
    else: 
        return {filtered.to_json(orient="records")}

@app.get('/rx/{value}/PAYER/{value2}')
async def rx2(value, value2):
    filtered = df[df['NUMBER_SCRIPTS'] == value]
    filtered2 = filtered[filtered['PAYER'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here.'}
    else: 
        return {filtered2.to_json(orient="records")}    
    