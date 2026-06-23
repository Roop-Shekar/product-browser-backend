import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from datetime import datetime
from app.db import get_connection

conn = get_connection()
cursor = conn.cursor()

for i in range(50):

    cursor.execute(
        """
        INSERT INTO products
        (
            name,
            category,
            price,
            created_at,
            updated_at
        )
        VALUES
        (
            %s,%s,%s,%s,%s
        )
        """,
        (
            f"New Product {i}",
            "Electronics",
            999.99,
            datetime.utcnow(),
            datetime.utcnow()
        )
    )

conn.commit()

cursor.close()
conn.close()

print("50 products inserted")