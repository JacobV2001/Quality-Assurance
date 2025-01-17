import psycopg2
import csv
import logging

logging.basicConfig(filename='data_import_errors.log', level=logging.ERROR)

def connect_db(host, user, password, database, port):
    # connect to postgres
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
    # close connection
    cursor.close()
    connection.close()

def insert_data_from_csv(file_path, query, columns):
    # insert data from csv into database

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) # move to the data - first row is labels
        for row in csv_reader:
            try: 
                data = tuple(row[index] for index in columns)
                my_cursor.execute(query, data)
                mydb.commit()
            except Exception as e:
                logging.error("Error inserting data: %s", e)
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

    # insert data specific to the csv
    insert_data_from_csv("sql-class/Subjects.csv", """INSERT INTO subjects (SubjectName) VALUES (%s)""", [1])
    insert_data_from_csv(
        "sql-class/Teachers.csv", 
        """INSERT INTO teachers (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email) VALUES (%s, %s, %s, %s, %s, %s)""",
        [1, 2, 3, 4, 5, 6]
    )
    insert_data_from_csv(
        "sql-class/Students.csv", 
        """INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email) VALUES (%s, %s, %s, %s, %s, %s)""",
        [1, 2, 3, 4, 5, 6]
    )
    insert_data_from_csv(
        "sql-class/Marks.csv",
        """INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate) VALUES (%s, %s, %s, %s, %s)""",
        [1, 2, 3, 4, 5]
    )

    close_db(mydb, my_cursor)