SELECT * FROM marks
WHERE StudentID = 2;

SELECT * FROM students;

DELETE FROM students
WHERE StudentID = 2; -- DELETE Student 2

-- All marks for student 2 deleted
SELECT * FROM marks
WHERE StudentID = 2;

-- Student 2 no longer in students
SELECT * FROM students;