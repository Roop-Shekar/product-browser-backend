import sys
import os
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
sys.path.append(project_root)
from app.db import get_connection

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
conn = get_connection()
cursor = conn.cursor()

cursor.execute(
    "TRUNCATE TABLE products RESTART IDENTITY;"
)

conn.commit()

cursor.close()
conn.close()

print("Products table cleared")