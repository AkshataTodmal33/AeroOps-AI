from llm import ask_llm


def generate_answer(question, sql, result):

    prompt = f"""
You are AeroOps AI, an aviation data analyst.

The user asked:

{question}

The SQL query was:

{sql}

The PostgreSQL database returned this result:

{result}

IMPORTANT COLUMN ORDER:

The flights table columns are:

1. flight_id
2. airline
3. source
4. destination
5. flight_date
6. delay_minutes
7. cancelled
8. distance_km

Therefore:

- Value 6 is ALWAYS delay_minutes.
- Value 7 is ALWAYS cancelled.
- Value 8 is ALWAYS distance_km.
- Never confuse distance_km with delay_minutes.

For the database result:

{result}

identify the values according to the column order above.

Rules:
1. Use ONLY the database result.
2. Do not invent information.
3. Never confuse delay_minutes and distance_km.
4. If the question asks about delay, use delay_minutes.
5. If the question asks about distance, use distance_km.
6. If the result is empty, say that no matching data was found.
7. Give a short, clear answer.
8. Do not mention the SQL query.

Return only the final answer.
"""

    answer = ask_llm(prompt)

    return answer