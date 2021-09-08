from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return "<h1>Hello World</h1>"

# New Route
@app.get("/login")
def login():
    return {"user": "daniel692a"}