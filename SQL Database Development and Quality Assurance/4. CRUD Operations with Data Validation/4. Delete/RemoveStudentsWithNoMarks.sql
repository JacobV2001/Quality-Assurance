-- insert student with no marks
INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('Tom', 'Hank', '2000-01-01', 'California, USA', 1000000000, 'Test@mail.gmail');

SELECT * FROM students;

DELETE FROM students
WHERE StudentID NOT IN (SELECT DISTINCT StudentID FROM marks);

SELECT * FROM students;
