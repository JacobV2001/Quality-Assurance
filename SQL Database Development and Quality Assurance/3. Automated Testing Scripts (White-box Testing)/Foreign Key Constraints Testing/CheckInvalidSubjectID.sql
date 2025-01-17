-- insert temp student
INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('John', 'Doe', '2000-01-01', 'Fresno, CA', '123-456-7890', 'john.doe@example.com');

-- Error due to no SubjectID
INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate)
VALUES (1, 999, 1, 80, '2025-01-01');
