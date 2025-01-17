import psycopg2

emails = [
    # valid emails
    "john.doe@mail.com",
    "jane_doe123@my-mail.org",
    "contact@company.co",
    "user.name+alias@gmail.com",
    "u@ab.co",
    "first.last@sub.domain.net",

    # invalid emails
    "plainaddress",            # No @ or domain
    "missingatsymbol.com",     # No @ 
    "@nodomain.com",           # Missing local
    "user@.com",               # Missing between @ and .
    "user@com.",               # Missing after .
    "user@domain",             # Missing tld
    "user@domain.c",           # TLD too short
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
    for email in emails:
        try:
            # insert the mark
            data = (email,)
            my_cursor.execute(query, data)
            mydb.commit()

            # delete mark so next test can work
            delete_data = (email,)
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

    # inser mark
    insert_marks_data(
        """INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email) VALUES ('John', 'Doe', '2000-01-01', 'Fresno, CA', 1234567890, %s)""",
        """DELETE FROM students WHERE Email = %s""")

    close_db(mydb, my_cursor)