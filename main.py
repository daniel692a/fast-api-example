from fastapi import FastAPI
from student import Student
from uuid import uuid4

app = FastAPI()

students = []


@app.get("/students")
def get_students():
    return students

@app.get("/")
def message():
    return "Welcome"

# @app.get("/user/{user_id}")
# def show_user(user_id: int):
#     """
#     Valid the value of user_id
#     The correct value must be an integer
#     """
#     return f"User id is: {user_id}"

@app.post("/add-student")
def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return f'{student.name} student saved'


@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student['id'] == student_id:
            return f'The student with id {student_id} is: {student}'
    return f'Student with id {student_id} not found'


@app.put('/students/{id}')
def update_student(id: str, updated_student: Student):
    for student in students:
        if student['id'] == id:
            student['name'] = updated_student.name
            student['last_name'] = update_student.last_name
            student['age'] = updated_student.age
            student['skills'] = updated_student.skills
            return f'Student with id {id} updated'
    return f'Student with id {id} not found'