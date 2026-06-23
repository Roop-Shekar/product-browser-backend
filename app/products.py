from datetime import datetime

from fastapi import APIRouter, Query, HTTPException

from app.db import get_connection, release_connection

router = APIRouter()


@router.get("/products")
def get_products(
    category: str | None = Query(default=None),
    cursor_updated_at: str | None = Query(default=None),
    cursor_id: int | None = Query(default=None),
    snapshot: str | None = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100)
):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # ------------------------------------------
        # Snapshot Validation
        # ------------------------------------------

        if snapshot:
            try:
                snapshot_time = datetime.fromisoformat(snapshot)
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid snapshot format. Use ISO format."
                )
        else:
            snapshot_time = datetime.utcnow()

        # ------------------------------------------
        # Cursor Validation
        # ------------------------------------------

        if cursor_updated_at:
            try:
                datetime.fromisoformat(cursor_updated_at)
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid cursor_updated_at format. Use ISO format."
                )

        # ------------------------------------------
        # CATEGORY FILTER
        # ------------------------------------------

        if category:

            # CATEGORY + CURSOR
            if cursor_updated_at is not None and cursor_id is not None:

                cursor.execute(
                    """
                    SELECT
                        id,
                        name,
                        category,
                        price,
                        created_at,
                        updated_at
                    FROM products
                    WHERE category = %s
                    AND updated_at <= %s
                    AND (updated_at, id) < (%s, %s)
                    ORDER BY updated_at DESC, id DESC
                    LIMIT %s
                    """,
                    (
                        category,
                        snapshot_time,
                        cursor_updated_at,
                        cursor_id,
                        limit
                    )
                )

            # CATEGORY + FIRST PAGE
            else:

                cursor.execute(
                    """
                    SELECT
                        id,
                        name,
                        category,
                        price,
                        created_at,
                        updated_at
                    FROM products
                    WHERE category = %s
                    AND updated_at <= %s
                    ORDER BY updated_at DESC, id DESC
                    LIMIT %s
                    """,
                    (
                        category,
                        snapshot_time,
                        limit
                    )
                )

        # ------------------------------------------
        # NO CATEGORY
        # ------------------------------------------

        else:

            # CURSOR PAGE
            if cursor_updated_at is not None and cursor_id is not None:

                cursor.execute(
                    """
                    SELECT
                        id,
                        name,
                        category,
                        price,
                        created_at,
                        updated_at
                    FROM products
                    WHERE updated_at <= %s
                    AND (updated_at, id) < (%s, %s)
                    ORDER BY updated_at DESC, id DESC
                    LIMIT %s
                    """,
                    (
                        snapshot_time,
                        cursor_updated_at,
                        cursor_id,
                        limit
                    )
                )

            # FIRST PAGE
            else:

                cursor.execute(
                    """
                    SELECT
                        id,
                        name,
                        category,
                        price,
                        created_at,
                        updated_at
                    FROM products
                    WHERE updated_at <= %s
                    ORDER BY updated_at DESC, id DESC
                    LIMIT %s
                    """,
                    (
                        snapshot_time,
                        limit
                    )
                )

        rows = cursor.fetchall()

        products = []

        for row in rows:
            products.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": float(row[3]),
                    "created_at": row[4].isoformat(),
                    "updated_at": row[5].isoformat()
                }
            )

        next_cursor = None

        if products:
            last_product = products[-1]

            next_cursor = {
                "updated_at": last_product["updated_at"],
                "id": last_product["id"]
            }

        return {
            "count": len(products),
            "products": products,
            "next_cursor": next_cursor,
            "snapshot": snapshot_time.isoformat()
        }

    finally:
        cursor.close()
        release_connection(conn)