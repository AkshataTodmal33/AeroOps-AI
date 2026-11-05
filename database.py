import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="aeroops_db",
        user="postgres",
        password="Akshata@33",
        port="5433"
    )

    return connection