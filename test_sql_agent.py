from sql_agent import generate_sql


question = input("Ask your question: ")

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)