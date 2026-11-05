from database import get_connection


def execute_sql(sql):

    sql_clean = sql.strip().lower()

    # Security check
    if not sql_clean.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    forbidden_keywords = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "create",
        "truncate",
        "grant",
        "revoke"
    ]

    for keyword in forbidden_keywords:
        if keyword in sql_clean:
            raise ValueError(
                f"Unsafe SQL detected: {keyword}"
            )

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows