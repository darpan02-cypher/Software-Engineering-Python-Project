from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "Hello World from POST"}


@app.put("/")
async def put():
    return {"message": "Hello World from PUT"}


###just for fun###
@app.delete("/")
async def delete():
    return {"message": "Hello World from DELETE"}
