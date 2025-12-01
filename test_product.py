from product import product_details

def test_product_details():
    output = product_details("P102", "Laptop", 5, 55000)

    expected = (
        "Product ID: P102\n"
        "Product Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 55000"
    )

    assert output == expected
