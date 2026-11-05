import pandas as pd
import psycopg2

# Step 1: Read CSV
df = pd.read_csv("data/flights.csv")

print("CSV loaded successfully!")
print(df)

# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="aeroops_db",
    user="postgres",
    password="Akshata@33",
    port="5433"
)

print("Connected to PostgreSQL!")

cursor = conn.cursor()

# Step 3: Insert data into flights table
for _, row in df.iterrows():

    cursor.execute("""
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
    """, (
        row["flight_id"],
        row["airline"],
        row["source"],
        row["destination"],
        row["flight_date"],
        row["delay_minutes"],
        row["cancelled"],
        row["distance_km"]
    ))

# Step 4: Save changes
conn.commit()

print("All flight records inserted successfully!")

# Step 5: Close connection
cursor.close()
conn.close()