import pytest
import pandas as pd
from app.preprocessor import create_orders_dataframe, create_products_dataframe
import json
import io

def test_orders_dataframe():
    sample_orders = [
        "2025-02-20, Order ID: 1001, Customer: Vishnu, Product: Laptop, Price: 75000, Status: Delivered",
        "2025-02-21, Order ID: 1002, Customer: Arjun, Product: Smartphone, Price: 45000, Status: Shipped",
        "2025-02-22, Order ID: 1003, Customer: Rahul, Product: Headphones, Price: 3000, Status: Processing",
        "2025-02-23, Order ID: 1004, Customer: Kiran, Product: Smartwatch, Price: 12000, Status: Delivered",
        "2025-02-24, Order ID: 1005, Customer: Priya, Product: Gaming Console, Price: 55000, Status: Cancelled"
    ]

    result = create_orders_dataframe(sample_orders)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty  # Ensure the dataframe is not empty
    assert "Order ID" in result.columns  # Check if a key column exists
    assert result.shape[0] == 5  # Ensure five orders are processed

def test_products_dataframe():
    sample_products = {
        "store": "TechBazaar",
        "category": "Electronics",
        "products": [
            {
                "id": 101,
                "name": "Laptop",
                "brand": "Dell",
                "price": 75000,
                "stock": 20,
                "ratings": 4.5
            },
            {
                "id": 102,
                "name": "Smartphone",
                "brand": "Samsung",
                "price": 45000,
                "stock": 50,
                "ratings": 4.3
            },
            {
                "id": 103,
                "name": "Smartwatch",
                "brand": "Apple",
                "price": 30000,
                "stock": 15,
                "ratings": 4.7
            }
        ]
    }

    sample_json = json.dumps(sample_products, indent=4)
    file_like_object = io.StringIO(sample_json)
    _, result = create_products_dataframe(file_like_object)

    assert isinstance(result, pd.DataFrame)
    assert not result.empty  # Ensure the dataframe is not empty
    assert "name" in result.columns  # Check if a key column exists
    assert result.shape[0] == 3  # Ensure three products are processed
