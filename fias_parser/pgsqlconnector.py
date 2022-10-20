import psycopg2 as psycopg2


def pgsqlConnection():
    return psycopg2.connect(
        "dbname=fias user=postgres password=postgres host=127.0.0.1 port=5432"
    )