import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.db import get_connection
from faker import Faker
from random import choice, uniform
from datetime import timedelta

from psycopg2.extras import execute_values



fake = Faker()

TOTAL_PRODUCTS = 200000
BATCH_SIZE = 5000

categories = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

conn = get_connection()
cursor = conn.cursor()

insert_query = """
INSERT INTO products
(
    name,
    category,
    price,
    created_at,
    updated_at
)
VALUES %s
"""

inserted = 0

while inserted < TOTAL_PRODUCTS:

    batch = []

    for _ in range(BATCH_SIZE):

        created_at = fake.date_time_between(
            start_date="-2y",
            end_date="now"
        )

        updated_at = created_at + timedelta(
            days=fake.random_int(0, 30)
        )

        batch.append(
            (
                fake.word().title() + " Product",
                choice(categories),
                round(uniform(100, 10000), 2),
                created_at,
                updated_at
            )
        )

    execute_values(
        cursor,
        insert_query,
        batch
    )

    conn.commit()

    inserted += BATCH_SIZE

    print(
        f"Inserted {inserted}/{TOTAL_PRODUCTS}"
    )

cursor.close()
conn.close()

print("Finished seeding 200000 products")