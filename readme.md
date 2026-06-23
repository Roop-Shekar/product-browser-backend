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
```

2. Create a virtual environment.

```bash
python -m venv venv
```

3. Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

4. Install the required packages.

```bash
pip install -r requirements.txt
```

5. Create a `.env` file and add your database credentials.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=productdb
DB_USER=postgres
DB_PASSWORD=your_password
```

6. Start the application.

```bash
uvicorn app.main:app --reload
```

7. Open the API documentation.

```text
http://127.0.0.1:8000/docs
```

## Usage

The application provides endpoints for retrieving products and product counts.

Get all products:

```http
GET /products
```

Filter products by category:

```http
GET /products?category=Electronics
```

Retrieve the next page using cursor pagination:

```http
GET /products?cursor_updated_at=<timestamp>&cursor_id=<id>
```

Get total product count:

```http
GET /products/count
```

## Results

The application successfully supports browsing a large dataset while maintaining good performance.

Key outcomes include:

- Efficient retrieval of products using indexed queries.
- Stable product ordering based on update timestamps.
- Consistent pagination during concurrent data modifications.
- Fast response times compared to traditional OFFSET-based pagination.

Example API Response:

```json
{
  "products": [
    {
      "id": 101,
      "name": "Wireless Headphones",
      "category": "Electronics",
      "price": 2999.00,
      "updated_at": "2026-06-20T10:15:00"
    }
  ],
  "next_cursor": {
    "updated_at": "2026-06-20T10:15:00",
    "id": 101
  }
}
```

Screenshots of Swagger documentation and API responses can be added here.

## Learning Outcomes

During the development of this project, the following concepts were learned and applied:

- FastAPI application development.
- REST API design principles.
- PostgreSQL database integration.
- Cursor-based pagination techniques.
- Snapshot-based consistency handling.
- Database indexing and query optimization.
- Environment variable management.
- Backend project structuring and organization.

## Future Improvements

- Add user authentication and authorization.
- Implement product search functionality.
- Add caching for frequently requested data.
- Support additional filtering and sorting options.
- Containerize the application using Docker.
- Deploy the application to a cloud platform.
- Add automated testing and CI/CD pipelines.

## Author

Roop Shekar Veeranki  
Student ID: SE23UCSE185

## License

This project was developed for academic and learning purposes only.
