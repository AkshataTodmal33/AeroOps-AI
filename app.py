from fastapi import FastAPI
from database import get_connection

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to AeroOps AI"
    }


@app.get("/flights")
def get_flights():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM flights ORDER BY flight_id")

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    flights = []

    for row in rows:
        flights.append({
            "flight_id": row[0],
            "airline": row[1],
            "source": row[2],
            "destination": row[3],
            "flight_date": str(row[4]),
            "delay_minutes": row[5],
            "cancelled": row[6],
            "distance_km": row[7]
        })

    return {
        "total_flights": len(flights),
        "flights": flights
    }

@app.get("/data-quality")
def data_quality():

    connection = get_connection()
    cursor = connection.cursor()

    # 1. Record count
    cursor.execute("SELECT COUNT(*) FROM flights")
    total_records = cursor.fetchone()[0]

    # 2. NULL check
    cursor.execute("""
        SELECT COUNT(*)
        FROM flights
        WHERE flight_id IS NULL
           OR airline IS NULL
           OR source IS NULL
           OR destination IS NULL
           OR flight_date IS NULL
           OR delay_minutes IS NULL
           OR cancelled IS NULL
           OR distance_km IS NULL
    """)

    null_records = cursor.fetchone()[0]

    # 3. Duplicate check
    cursor.execute("""
        SELECT COUNT(*)
        FROM (
            SELECT flight_id
            FROM flights
            GROUP BY flight_id
            HAVING COUNT(*) > 1
        ) duplicates
    """)

    duplicate_flight_ids = cursor.fetchone()[0]

    # 4. Invalid delay check
    cursor.execute("""
        SELECT COUNT(*)
        FROM flights
        WHERE delay_minutes < 0
    """)

    invalid_delay_records = cursor.fetchone()[0]

    # 5. Invalid distance check
    cursor.execute("""
        SELECT COUNT(*)
        FROM flights
        WHERE distance_km <= 0
    """)

    invalid_distance_records = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    # Overall status
    if (
        null_records == 0
        and duplicate_flight_ids == 0
        and invalid_delay_records == 0
        and invalid_distance_records == 0
    ):
        overall_status = "PASS"
    else:
        overall_status = "FAIL"

    return {
        "overall_status": overall_status,
        "total_records": total_records,
        "null_records": null_records,
        "duplicate_flight_ids": duplicate_flight_ids,
        "invalid_delay_records": invalid_delay_records,
        "invalid_distance_records": invalid_distance_records
    }