from fastapi import FastAPI
from test_module1.math.caculate import sum, sub, mul


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/add/{a}/{b}")
def read_item(a: int, b: int):
    return {"result": sum(a, b)}

@app.get("/sub/{a}/{b}")
def read_item(a: int, b: int):
    return {"result": sub(a, b)}

@app.get("/mul/{a}/{b}")
def read_item(a: int, b: int):
    return {"result": mul(a, b)}