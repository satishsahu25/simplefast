from fastapi import FastAPI

app=FastAPI()


@app.get("/")
async def basic():
    return {"Hello"}

@app.get("/")
async def test(pmp=""):
    return {pmp}