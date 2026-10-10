from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib



app = FastAPI(title='TESTANDO A API')


ia = joblib.load('ia pronta.pkl')


@app.get('/recebendo')
async def dados():
 return{
   'resultado': 'Seja Bem Vindo'
}

class model (BaseModel):
  open: float
  high: float
  low: float
  close: float


@app.post('/prever')
async def dados(item: model):
 dados_entrada = pd.DataFrame([{
     'open': item.open,
     'high': item.high,
     'low': item.low,
     'close': item.close
     }])
 volume = ia.predict(dados_entrada)[0]
 return{
 'resultado': f'Valor previsto {volume[0]:,.2%}'
 }