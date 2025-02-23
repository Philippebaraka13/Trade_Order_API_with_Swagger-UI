from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI(title="Trade Order API")

DATABASE = "orders.db"

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            order_type TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

def insert_order(order: Order):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (symbol, price, quantity, order_type) VALUES (?, ?, ?, ?)",
        (order.symbol, order.price, order.quantity, order.order_type)
    )
    conn.commit()
    conn.close()

def get_all_orders() -> List[Order]:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, price, quantity, order_type FROM orders")
    rows = cursor.fetchall()
    conn.close()
    return [Order(symbol=row[0], price=row[1], quantity=row[2], order_type=row[3]) for row in rows]

@app.get("/", response_class=HTMLResponse)
def landing_page():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Trade Order API</title>
        <style>
          body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f7fa;
            color: #333;
          }
          .header {
            background: #333;
            color: #fff;
            padding: 15px;
          }
          .header h2 {
            margin: 0;
          }
          .container {
            max-width: 800px;
            margin: 40px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
          }
          a.button {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #007BFF;
            color: #fff;
            text-decoration: none;
            border-radius: 4px;
            transition: background 0.3s ease;
          }
          a.button:hover {
            background: #0056b3;
          }
          h1 {
            margin-top: 0;
          }
          ul {
            padding-left: 20px;
          }
        </style>
      </head>
      <body>
        <div class="header">
          <h2>Trade Order API</h2>
        </div>
        <div class="container">
          <h1>Welcome to the Trade Order API</h1>
          <p>This API allows you to create, retrieve, and manage trade orders seamlessly.</p>
          <ul>
            <li><strong>POST /orders:</strong> Submit a new order.</li>
            <li><strong>GET /orders:</strong> Retrieve all existing orders.</li>
            <li><strong>WebSocket /ws:</strong> Real-time updates (if implemented).</li>
          </ul>
          <p>
            To explore the API, click the button below to open our interactive documentation (Swagger UI), 
            or use any API testing tool like Postman to get started!
          </p>
          <a href="/docs" class="button">View API Documentation</a>
        </div>
      </body>
    </html>
    """

@app.post("/orders", status_code=201)
def create_order(order: Order):
    insert_order(order)
    return {"message": "Order created successfully"}

@app.get("/orders", response_model=List[Order])
def list_orders():
    return get_all_orders()
