from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce_store"]

# Define collections
products_collection = db["products"]
categories_collection = db["categories"]
customers_collection = db["customers"]
orders_collection = db["orders"]

# Insert Products
product1 = {
    "name": "Smartphone",
    "price": 699.99,
    "category": "Electronics",
    "stock_quantity": 50,
    "customer_reviews": [],
}
product2 = {
    "name": "Jeans",
    "price": 49.99,
    "category": "Clothing",
    "stock_quantity": 200,
    "customer_reviews": [],
}
products_collection.insert_many([product1, product2])

# Insert Categories
electronics_category = {
    "category_name": "Electronics",
    "description": "Electronic gadgets and devices",
    "products": [],  # Will be populated later with product IDs
}
clothing_category = {
    "category_name": "Clothing",
    "description": "Men and Women fashion wear",
    "products": [],  # Will be populated later with product IDs
}
categories_collection.insert_many([electronics_category, clothing_category])

# Fetch product IDs and update categories with product references
smartphone = products_collection.find_one({"name": "Smartphone"})
jeans = products_collection.find_one({"name": "Jeans"})

categories_collection.update_one(
    {"category_name": "Electronics"}, {"$push": {"products": smartphone["_id"]}}
)
categories_collection.update_one(
    {"category_name": "Clothing"}, {"$push": {"products": jeans["_id"]}}
)

# Insert Customers
customer1 = {
    "name": "John Doe",
    "address": "123 Main St, Springfield",
    "order_history": [],
}
customer2 = {
    "name": "Jane Smith",
    "address": "456 Oak St, Metropolis",
    "order_history": [],
}
customers_collection.insert_many([customer1, customer2])

# Fetch customer IDs
customer1 = customers_collection.find_one({"name": "John Doe"})
customer2 = customers_collection.find_one({"name": "Jane Smith"})

# Insert Orders
order1 = {
    "customer_id": customer1["_id"],
    "products_purchased": [
        {"product_id": smartphone["_id"], "quantity": 1},
        {"product_id": jeans["_id"], "quantity": 2},
    ],
    "total_amount": 799.97,
    "order_status": "Pending",
}
order2 = {
    "customer_id": customer2["_id"],
    "products_purchased": [{"product_id": jeans["_id"], "quantity": 1}],
    "total_amount": 49.99,
    "order_status": "Shipped",
}
orders_collection.insert_many([order1, order2])

# Fetch order IDs and update customer order history
order1 = orders_collection.find_one({"customer_id": customer1["_id"]})
order2 = orders_collection.find_one({"customer_id": customer2["_id"]})

customers_collection.update_one(
    {"_id": customer1["_id"]}, {"$push": {"order_history": order1["_id"]}}
)
customers_collection.update_one(
    {"_id": customer2["_id"]}, {"$push": {"order_history": order2["_id"]}}
)

print("Data insertion complete.")
