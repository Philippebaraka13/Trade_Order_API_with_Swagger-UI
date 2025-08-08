# tests/test_main.py
import os
import pytest
from fastapi.testclient import TestClient
from ..main import app, DATABASE, init_db

client = TestClient(app)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    init_db()
    yield


def test_landing_page():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Trade Order API" in response.content

def test_create_order():
    order_data = {
        "symbol": "AAPL",
        "price": 150.0,
        "quantity": 10,
        "order_type": "buy"
    }
    response = client.post("/orders", json=order_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Order created successfully"}

def test_list_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, list)
    assert len(orders) > 0
    first_order = orders[0]
    assert first_order["symbol"] == "AAPL"
    assert first_order["price"] == 150.0
    assert first_order["quantity"] == 10
    assert first_order["order_type"] == "buy"
