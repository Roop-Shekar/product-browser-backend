from app.db import get_connection

try:
    conn = get_connection()

    print("SUCCESS: Database Connected")

    conn.close()

except Exception as e:
    print("ERROR:")
    print(e) 