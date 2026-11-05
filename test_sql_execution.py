from sql_agent import generate_sql
from sql_executor import execute_sql


question = input("Ask your question: ")

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

try:

    result = execute_sql(sql)

    print("\nDatabase Result:")
    print(result)

except Exception as e:

    print("\nError:")
    print(e)