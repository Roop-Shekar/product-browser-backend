import sys
import os

# Add project root directory to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app.db import get_connection

conn = None
cursor = None

try:
    conn = get_connection()
    cursor = conn.cursor()

    with open("sql/indexes.sql", "r") as file:
        sql_script = file.read()

    cursor.execute(sql_script)

    conn.commit()

    print("Indexes created successfully")

except Exception as e:
    print(f"Error creating indexes: {e}")

finally:
    if cursor:
        cursor.close()

    if conn:
        conn.close()