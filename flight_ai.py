from flight_data import get_flight_data
from llm import ask_llm


# Get flight data from PostgreSQL
flights = get_flight_data()


# Convert flight data into text
flight_data_text = ""

for flight in flights:
    flight_data_text += str(flight) + "\n"


print("===================================")
print("        AeroOps AI Assistant       ")
print("===================================")

question = input("\nAsk your question: ")


prompt = f"""
You are AeroOps AI, an aviation data analyst.

You have been given flight data from a PostgreSQL database.

Flight data:

{flight_data_text}

Answer the user's question using ONLY the provided flight data.

If the answer cannot be found in the provided data,
say: "I don't have enough data to answer that."

User question:

{question}
"""


answer = ask_llm(prompt)


print("\nAI Answer:")
print(answer)