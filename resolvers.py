from random import randint

students = {1: {"id": 1, "name": "Pallavi"}}
classes = {1: {"id":1, "name": "CMPE273", "students": []}}

def get_student(_, _info, id):
    return students[id]

def get_class(_, _info, id):
    return classes[id]

def create_student(_, _info, name):
    id = randint(10000, 20000)
    students[id] = {"id": id, "name": name}
    return students[id]

def create_class(_, _info, name):
    id = randint(100, 300)
    classes[id] = {"id": id, "name": name, "students": []}
    return classes[id]

def update_class(_, _info, student_id, class_id):
    classes[class_id]["students"].append(students[student_id])
    return classes[class_id]
