from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import get_connection, release_connection
from app.products import router as products_router

app = FastAPI(
    title="Product Browser API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Product Routes
app.include_router(products_router)


@app.get("/")
def root():
    return {
        "status": "running"
    }


@app.get("/health")
def health_check():

    conn = None

    try:
        conn = get_connection()

        return {
            "database": "connected"
        }

    except Exception as e:

        return {
            "database": "failed",
            "error": str(e)
        }

    finally:
        if conn:
            release_connection(conn)


@app.get("/products/count")
def product_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM products"
    )

    count = cursor.fetchone()[0]

    cursor.close()
    release_connection(conn)

    return {
        "total_products": count
    }