import mysql.connector
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

# Defining the global variables
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")
USER = os.getenv("USER")
CURRENT_DATABASE = os.getenv("CURRENT_DATABASE")


@contextmanager
def get_cursor(host, user, password, database):
    """
    build the connection with your mysql and create the cursor object
    
    :param host: mysql host
    :param user: mysql username
    :param password: your mysql password
    :param database: current database
    :return: connection and cursor dictionary
    """
    connection = mysql.connector.connect(
        host=host,
        user = user,
        password = password,
        database = database
    )
    # checking if the connection is established
    if connection.is_connected():
        print("Connection success!!")
    else:
        print("Failed in Connection!")


    cursor = connection.cursor(dictionary=True)
    yield cursor

    cursor.close()
    connection.close()
    

def fetchall_data():
    """
    Fetching all the data
    """
    with get_cursor(HOST, USER, PASSWORD, CURRENT_DATABASE) as cursor:
        cursor.execute("SELECT * FROM expenses;")
        expenses = cursor.fetchall()

        for exp in expenses:
            print(exp)


def fetchall_expenses_for_date(expense_date):
    """
    list down everything happened on the expense_date
    
    :param expense_date: desired date
    :return: dictionary of data for the selected  date
    """
    with get_cursor(HOST, USER, PASSWORD, CURRENT_DATABASE) as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date == %s;", (expense_date,))
        expenses = cursor.fetchall()

        for exp in expenses:
            print(exp)

if __name__ == "__main__":
    fetchall_data()