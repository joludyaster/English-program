import sqlite3
from sqlite3 import Error


def create_connection_to_the_database(db_file):

    """
    Create a database connection to the SQLite database specified by db_file

    :param db_file: database file
    :return: connection object or None
    """

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table_in_the_database(connection, sql_table):

    """
    Create a table from the sql_table statement

    :param connection: connection object
    :param sql_table: a CREATE TABLE statement
    :return:
    """

    try:
        cursor = connection.cursor()
        cursor.execute(sql_table)
    except Error as e:
        print(e)


def insert_data_in_the_database(connection, data):

    """
    Create a new used column into the data sql table

    :param connection: connection object
    :param data: the data, that needs to be inserted into the database
    :return:
    """

    table = '''INSERT INTO data (email, username, password, dictionary, signing_in) VALUES (?, ?, ?, ?, ?)'''
    cursor = None

    try:
        cursor = connection.cursor()
        cursor.execute(table, data)
        connection.commit()
    except Error as e:
        print(f"The error {e} occurred!")

    return cursor.lastrowid


def update_data_in_the_database(connection, data, task):

    """
    Update a data in the database
    
    :param data: the data, that needs to be updated in the database
    :param connection: connection object
    :param task: list of the data that will be inserted into the database
    :return:
    """
    table = f'''UPDATE data SET {data} WHERE email = ?'''

    try:
        cursor = connection.cursor()
        cursor.execute(table, task)
        connection.commit()
    except Error as e:
        print(f"The error {e} occurred!")


def select_data_in_the_database(connection, data, condition):

    """
    Select the specific data from database

    :param connection: connection object
    :param data: the data, that needs to be selected from the database
    :param condition: condition to get data from specific column
    :return: selectedData object with data inside
    """
    cursor = None
    selectedData = None

    try:
        cursor = connection.cursor()
        if condition:
            cursor.execute(f'''SELECT {data} FROM data WHERE email = ?''', [condition])
        else:
            cursor.execute(f'''SELECT {data} FROM data''')

        selectedData = cursor.fetchall()
    except Error as e:
        print(f"The error {e} occurred!")

    return selectedData

# def create_connection_for_create_db(db_name):
#     connection = None
#     try:
#         connection = connect(database=db_name,
#                              user="postgres",
#                              password="password",
#                              host="localhost",
#                              port=5432)
#         print("Connection to PostgreSQL DB successful")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection
#
#
# def create_database_for_create_db(connection, query):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#
#
# def create_datab(db_name, title_of_database):
#     if create_connection_for_create_db(db_name):
#         pass
#     else:
#         connection = create_connection_for_create_db(db_name)
#         create_database_query_for_create_db = f"CREATE DATABASE {title_of_database}"
#         create_database_for_create_db(connection, create_database_query_for_create_db)
