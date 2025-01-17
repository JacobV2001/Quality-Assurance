import psycopg2

numbers = [
    # valid phone numbers
    "+1 (123) 456-7890",
    "1234567890",
    "123-456-7890",
    "(123) 456-7890",
    "123 456 7890",
    "+91 9876543210",
    "(123 456-7890",
    "123) 456-7890",
    "123 456-7890  ",

    
    # invalid phone numbers
    "1234567",                 # Less than 10 numbers
    "abcdefghij",              # Non number Characters
    "123-4567-890!"            # Special Character
]


def connect_db(host, user, password, database, port):
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            port = port
        )

        cursor = connection.cursor()
        return connection, cursor
    except Exception as e:
        print("Error connecting to the database: ", e)
        exit(1)

def close_db(connection, cursor):
    cursor.close()
    connection.close()

def insert_marks_data(query, delete_query):
    for number in numbers:
        try:
            data = (number,)
            my_cursor.execute(query, data)
            mydb.commit()

            delete_data = (number,)
            my_cursor.execute(delete_query, delete_data)
            mydb.commit()

        except Exception as e:
            print("An error occured ", e)
            mydb.rollback()
            

if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "user": "postgres",
        "password": "root",
        "database": "sql-class",
        "port": 5432
    }

    mydb, my_cursor = connect_db(**db_config)

    insert_marks_data(
        """INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email) VALUES ('John', 'Doe', '2000-01-01', 'Fresno, CA', %s, 'JohnDoe@mail.com')""",
        """DELETE FROM students WHERE ContactNumber = %s""")

    close_db(mydb, my_cursor)