# Product Browser Backend

## Overview

This project is a backend application developed using FastAPI and PostgreSQL to efficiently browse a large product catalog containing approximately 200,000 products. The system supports category-based filtering, fast pagination, and maintains consistent results even when products are added or updated while users are browsing.

The project was developed as part of a backend engineering assignment to demonstrate database design, API development, and efficient pagination techniques for large datasets.

## Objectives

- Build a scalable backend capable of handling a large number of products.
- Implement fast and efficient pagination without relying on OFFSET queries.
- Provide category-based product filtering.
- Ensure users do not see duplicate or missing products while browsing if data changes in the database.
- Design clean and maintainable API endpoints.

## Features

- Browse products sorted by latest updates.
- Filter products by category.
- Cursor-based pagination for better performance.
- Snapshot-based pagination consistency.
- RESTful API built with FastAPI.
- PostgreSQL database integration.
- Database indexing for optimized query execution.
- Interactive API documentation using Swagger UI.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- Psycopg2
- Uvicorn
- Python-dotenv

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
cd product-browser-backend
