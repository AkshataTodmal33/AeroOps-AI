from database import get_connection


def get_flight_data():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            flight_id,
            airline,
            source,
            destination,
            flight_date,
            delay_minutes,
            cancelled,
            distance_km
        FROM flights
        ORDER BY flight_id
    """)

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

    return flights