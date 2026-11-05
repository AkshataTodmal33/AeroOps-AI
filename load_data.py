import csv
import psycopg2

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="aeroops_db",
    user="postgres",
    password="Akshata@33",
    port="5433"
)

cursor = connection.cursor()

# Read CSV file
with open("data/flights.csv", "r") as file:

    reader = csv.DictReader(file)

    # Insert each row into PostgreSQL
    for row in reader:

        cursor.execute(
            """
            INSERT INTO flights
            (
                flight_id,
                airline,
                source,
                destination,
                flight_date,
                delay_minutes,
                cancelled,
                distance_km
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["flight_id"],
                row["airline"],
                row["source"],
                row["destination"],
                row["flight_date"],
                int(row["delay_minutes"]),
                row["cancelled"].lower() == "true",
                int(row["distance_km"])
            )
        )

# Save the changes
connection.commit()

cursor.close()
connection.close()

print("CSV data loaded successfully!")