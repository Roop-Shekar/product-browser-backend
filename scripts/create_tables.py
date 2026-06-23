import sys
import os
from app.db import get_connection
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.db import get_connection

conn = get_connection()
cursor = conn.cursor()

with open("sql/schema.sql", "r") as file:
    sql_script = file.read()

cursor.execute(sql_script)

conn.commit()

cursor.close()
conn.close()

print("Products table created successfully")