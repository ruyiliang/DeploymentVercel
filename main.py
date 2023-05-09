from fastapi import FastAPI 
import pandas as pd 

df = pd.read_csv('./data/utilization2018.csv')

app = FastAPI()

@app.get('/')
async def root():
    return {'This is a API service for MN Healthcare Utilization details from 2018.'}

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return {result}

@app.get("/ctycd/{value}")
async def ctycdcode(value):
    print('value: ', value)
    filtered = df[df['county_code'] == value]
    if len(filtered) <= 0:
        return {'There is nothing here.'}
    else: 
        return {filtered.to_json(orient="records")}

@app.get('/ctycd/{value}/sex/{value2}')
async def ctycdcode2(value, value2):
    filtered = df[df['county_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return {'There is nothing here.'}
    else: 
        return {filtered2.to_json(orient="records")}    
    