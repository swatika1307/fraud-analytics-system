import mysql.connector
import pandas as pd

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Swatika@2001",
        database="fraud_analytics_db"
    )

    return connection


def run_query(query):
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

        df = pd.DataFrame(rows, columns=columns)

        cursor.close()

        return df

    finally:
        connection.close()