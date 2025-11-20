from fastapi import FastAPI 


app = FastAPI()

@app.get("/")

def test():
    return {"test":"working"}

@app.get("/hi")

def gg():
    return {"hi"}

