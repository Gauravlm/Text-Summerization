from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import Predictionpipeline 

text:str = 'What is Text Summarization?'

app = FastAPI()
@app.get('/',tags=['authentication'])
async def index():
    return RedirectResponse(url='/docs')

#for training 

@app.get('/train')
async def training():
    try:
        os.system('python main.py')
        return Response('Training Successful...!')
    except Exception as e:
        return Response(f'Error occured while Training {e}')

@app.post('/predict')
async def predict_route(text):
    try:
        obj = Predictionpipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__== '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8080)
    