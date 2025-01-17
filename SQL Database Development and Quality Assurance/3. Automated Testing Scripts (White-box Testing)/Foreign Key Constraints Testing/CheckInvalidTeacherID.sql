-- insert temp student
INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('John', 'Doe', '2000-01-01', 'Fresno, CA', '123-456-7890', 'john.doe@example.com');

-- insert temp subject
INSERT INTO subjects (SubjectName)
VALUES ('Mathematics');

-- Error due to no matching TeacherID
INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate)
VALUES (1, 1, 999, 80, '2025-01-01'); 