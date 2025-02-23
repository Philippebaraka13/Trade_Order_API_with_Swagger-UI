# Trade Order API

A simple backend service built with FastAPI that accepts and retrieves trade orders. The API supports REST endpoints for creating and listing orders, and includes an optional WebSocket endpoint for real-time updates.
![Screenshot 2025-02-23 164550](https://github.com/user-attachments/assets/15c3c79c-6872-4fa4-935b-0c08c5b74b8b)

## Features

- **POST /orders:** Submit a trade order (symbol, price, quantity, order type).
- **GET /orders:** Retrieve all submitted orders.
- **SQLite:** Simple database for order storage.
- **Docker:** Containerized application.
- **CI/CD:** Automated testing and deployment via GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.10
- Docker (if containerizing)
- Git

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
2. Run the FastAPI server.
   ```bash
   uvicorn main:app --reload
   
3. Access the API docs
   ```bash
   http://127.0.0.1:8000/docs
