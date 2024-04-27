from fastapi import FastAPI

app = FastAPI()

@app.get('/is_running')
def is_running():
    return {"running": True}

@app.get('/')
def is_running():
    return {"homepage": "this is a homepage"}