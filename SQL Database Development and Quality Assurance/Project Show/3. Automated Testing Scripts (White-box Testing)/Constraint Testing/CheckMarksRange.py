import psycopg2

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

# attempt to insert marks from range -1 -> 101
def insert_marks_data(query, delete_query):
    for mark in range (-1, 102):
        try:
            data = (mark,)
            my_cursor.execute(query, data)
            mydb.commit()

            delete_data = (mark,)
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
        """INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate) VALUES (1, 1, 1, %s, '2024-01-01')""",
        """DELETE FROM marks WHERE MarkObtained = %s""")

    close_db(mydb, my_cursor)