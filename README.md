# Trade Order API

A simple backend service built with FastAPI that accepts and retrieves trade orders. The API supports REST endpoints for creating and listing orders, and includes an optional WebSocket endpoint for real-time updates.

## Features

- **POST /orders:** Submit a trade order (symbol, price, quantity, order type).
- **GET /orders:** Retrieve all submitted orders.
- **WebSocket /ws:** Optional endpoint for real-time order updates.
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
