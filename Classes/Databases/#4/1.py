from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)  # Replace with your MongoDB connection string if necessary
db = client["myfirstdb"]  # Create or connect to 'myfirstdb' database
collection = db["students"]  # Create or connect to 'students' collection

student = {"name": "John Doe", "age": 21, "major": "Computer Science"}

insert_result = collection.insert_one(student)  # Insert one document
print(f"Inserted student with _id: {insert_result.inserted_id}")

all_students = collection.find()  # Find all documents
print("All students:")
for student in all_students:
    print(student)
