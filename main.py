from fastapi import FastAPI
from student import Student

app = FastAPI()

@app.get("/")
def message():
    return "<h1>Hello World</h1>"

# New Route
@app.get("/login")
def login():
    return "Ingrese sus datos"

@app.get("/user/{user_id}")
def show_user(user_id: int):
    """
    Valid the value of user_id
    The correct value must be an integer
    """
    return f"User id is: {user_id}"

@app.post("/students")
def save_student(student: Student):
    return f"{student.name} {student.last_name} skills: {student.skills}"