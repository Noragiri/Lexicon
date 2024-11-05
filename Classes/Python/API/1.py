import requests

API_URL = "https://fakestoreapi.com/products"


def show_all_products():
    response = requests.get(API_URL)
    products = response.json()
    print("\nAll Products:")
    for product in products:
        print(f"- {product['title']}")


def show_product_details():
    product_id = input("\nEnter the product ID you want to see details for: ")
    response = requests.get(f"{API_URL}/{product_id}")

    if response.status_code == 200:
        product = response.json()
        print("\nProduct Details:")
        print(f"Name: {product['title']}")
        print(f"Price: ${product['price']}")
        print(f"Description: {product['description']}")
        print(f"Category: {product['category']}")
    else:
        print("Product not found.")


def add_new_product():
    title = input("\nEnter product name: ")
    price = float(input("Enter price: "))
    description = input("Enter product description: ")
    category = input("Enter category: ")

    new_product = {
        "title": title,
        "price": price,
        "description": description,
        "category": category,
        "image": "https://fakestoreapi.com/img/placeholder.png",
    }

    response = requests.post(API_URL, json=new_product)
    if response.status_code == 200:
        added_product = response.json()
        print("\nProduct added:")
        print(added_product)
    else:
        print("Failed to add product.")


def main():
    while True:
        print("\nMenu:")
        print("1. Show all products")
        print("2. Show product details")
        print("3. Add a new product")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_all_products()
        elif choice == "2":
            show_product_details()
        elif choice == "3":
            add_new_product()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
