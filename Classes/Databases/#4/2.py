from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)  # Replace with your MongoDB connection string
db = client["library_system"]  # Create or connect to 'library_system' database

books_collection = db["books"]
authors_collection = db["authors"]
users_collection = db["users"]

books = [
    {
        "title": "1984",
        "genre": "Dystopian",
        "author": "George Orwell",
        "published_year": 1949,
    },
    {
        "title": "The Great Gatsby",
        "genre": "Fiction",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
    },
    {
        "title": "To Kill a Mockingbird",
        "genre": "Fiction",
        "author": "Harper Lee",
        "published_year": 1960,
    },
    {
        "title": "Moby-Dick",
        "genre": "Adventure",
        "author": "Herman Melville",
        "published_year": 1851,
    },
    {
        "title": "Pride and Prejudice",
        "genre": "Romance",
        "author": "Jane Austen",
        "published_year": 1813,
    },
]

authors = [
    {"name": "George Orwell", "birthdate": "1903-06-25", "nationality": "British"},
    {
        "name": "F. Scott Fitzgerald",
        "birthdate": "1896-09-24",
        "nationality": "American",
    },
    {"name": "Harper Lee", "birthdate": "1926-04-28", "nationality": "American"},
    {"name": "Herman Melville", "birthdate": "1819-08-01", "nationality": "American"},
    {"name": "Jane Austen", "birthdate": "1775-12-16", "nationality": "British"},
]

users = [
    {
        "name": "Alice",
        "email": "alice@example.com",
        "borrowed_books": ["1984", "Moby-Dick"],
    },
    {"name": "Bob", "email": "bob@example.com", "borrowed_books": ["The Great Gatsby"]},
    {
        "name": "Charlie",
        "email": "charlie@example.com",
        "borrowed_books": ["To Kill a Mockingbird", "Pride and Prejudice"],
    },
    {"name": "David", "email": "david@example.com", "borrowed_books": []},
    {"name": "Eve", "email": "eve@example.com", "borrowed_books": ["1984"]},
]
try:
    books_collection.insert_many(books)
    authors_collection.insert_many(authors)
    users_collection.insert_many(users)
    print("Data inserted into collections!")
except ValueError:
    print(ValueError)

recent_books = books_collection.find({"published_year": {"$gt": 2000}})
print("Books published after the year 2000:")
for book in recent_books:
    print(book)

users_collection.update_one(
    {"name": "Alice"}, {"$set": {"borrowed_books": ["1984", "Pride and Prejudice"]}}
)

books_collection.delete_one({"title": "Moby-Dick"})
print("Deleted 'Moby-Dick' from the collection.")

sorted_books = books_collection.find().sort("published_year", 1)
print("Books sorted by publication year:")
for book in sorted_books:
    print(book)
