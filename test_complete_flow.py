from sql_agent import generate_sql
from sql_executor import execute_sql
from answer_generator import generate_answer


question = input("Ask your question: ")

# Step 1: Generate SQL
sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)


# Step 2: Execute SQL
try:
    result = execute_sql(sql)

    print("\nDatabase Result:")
    print(result)

except Exception as e:
    print("\nSQL Execution Error:")
    print(e)
    exit()


# Step 3: Generate natural-language answer
answer = generate_answer(
    question,
    sql,
    result
)

print("\n===================================")
print("          AeroOps AI Answer")
print("===================================")
print(answer)