from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
import requests

app = FastAPI()

headers = {'Content-Type': 'application/json'}
data = '{}'

@app.get('/')
def hello_world():
    return 'Hello Agones!'

@app.get('/shutdown')
def shutdown():
    response = requests.post('http://localhost:9358/shutdown', headers=headers, data=data)
    return 'shutdown'

@app.get('/reset')
def reset():
    response = requests.post('http://localhost:9358/ready', headers=headers, data=data)
    return 'game server reset'    

@app.on_event("startup")
def ready():
    response = requests.post('http://localhost:9358/ready', headers=headers, data=data)
    return response

@app.on_event("startup")
@repeat_every(seconds=3)
def healthcheck():
    response = requests.post('http://localhost:9358/health', headers=headers, data=data)
    return response
