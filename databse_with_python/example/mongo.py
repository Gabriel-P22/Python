from pymongo import MongoClient


mongo_url = "mongodb://localhost:27017/"
client = MongoClient(mongo_url)

db = client["school"]
students = db["students"]

student_model = {
    "name": "Gabriel",
    "age": 24
}

students.insert_one(student_model)

for student in students.find():
    print(student)
