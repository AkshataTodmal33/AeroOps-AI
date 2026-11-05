from llm import ask_llm


def generate_sql(question):

    prompt = f"""
You are a PostgreSQL SQL expert for an aviation operations system.

We have a table called flights.

Table columns:

- flight_id VARCHAR
- airline VARCHAR
- source VARCHAR
- destination VARCHAR
- flight_date DATE
- delay_minutes INTEGER
- cancelled BOOLEAN
- distance_km INTEGER

Convert the user's question into a PostgreSQL SELECT query.

IMPORTANT RULES:

1. Generate ONLY a SELECT query.
2. Do not use INSERT.
3. Do not use UPDATE.
4. Do not use DELETE.
5. Do not use DROP.
6. Do not use ALTER.
7. Do not use CREATE.
8. Do not add markdown.
9. Do not explain the query.
10. Always return enough columns to answer the user's question completely.
11. Do not return only an ID if the user asks about a flight.
12. If the question asks for the flight with the highest delay, return:
    flight_id, airline, source, destination, flight_date,
    delay_minutes, cancelled.
13. If the question asks about distance, include distance_km.
14. If the question asks for airline-level statistics, include the airline and the requested calculation.
15. Use the correct column for the requested measurement.

Examples:

Question:
Which flight has the highest delay?

SQL:
SELECT flight_id, airline, source, destination, flight_date,
       delay_minutes, cancelled
FROM flights
ORDER BY delay_minutes DESC
LIMIT 1;

Question:
Which flight has the longest distance?

SQL:
SELECT flight_id, airline, source, destination, flight_date,
       delay_minutes, cancelled, distance_km
FROM flights
ORDER BY distance_km DESC
LIMIT 1;

Question:
How many flights does Air India operate?

SQL:
SELECT COUNT(*)
FROM flights
WHERE airline = 'Air India';

User question:

{question}
"""

    sql = ask_llm(prompt)

    return sql.strip()