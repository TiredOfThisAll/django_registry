import psycopg2

def create_connection():
    connection = psycopg2.connect(dbname="reestr_db", user="postgres", password="123321", host="127.0.0.1")
    return connection
