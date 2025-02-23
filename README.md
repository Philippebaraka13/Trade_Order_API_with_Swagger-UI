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


# Project Architecture

This project leverages a modern stack to deliver a scalable and maintainable application. Below is an overview of the architecture and key components:

## Backend

- **FastAPI**  
  - Serves as the backbone for REST endpoints.
  - Supports optional WebSocket communication for real-time features.

## Database

- **SQLite**  
  - Utilized as a local file for storing orders.
  - For production environments, consider using **PostgreSQL** for enhanced performance and scalability.

## Containerization

- **Docker**  
  - Containerizes the FastAPI application.
  - Ensures consistency across development and production environments.

## Production Environment

- **AWS EC2 (Ubuntu)**  
  - Hosts the Docker container.
  - Provides a reliable infrastructure for deployment.

## CI/CD Pipeline

- **GitHub Actions**  
  - **Testing:** Runs tests on all pull requests to ensure code quality.
  - **Docker Integration:** Builds and pushes Docker images to Docker Hub.
  - **Deployment:** SSHs into the EC2 instance for seamless deployment.

