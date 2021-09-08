from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return "<h1>Hello World</h1>"

# New Route
@app.get("/login")
def login():
    return "Ingrese sus datos"

@app.get("/user/{user_id}")
def show_user(user_id):
    return f"User id is: {user_id}"