import pytest
def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


# Example call (not required for pytest)
if __name__ == "__main__":
    product_id = "P102"
    product = "Laptop"
    quantity = "5"
    price = "55000"

    print(product_details("P102", "Laptop", 5, 55000))
