SELECT s.FirstName, s.LastName, sub.SubjectName, t.FirstName AS TeacherFirstName, t.LastName AS TeacherLastName, 
       m.MarkObtained, m.ExamDate
FROM marks m
JOIN students s ON m.StudentID = s.StudentID
JOIN subjects sub ON m.SubjectID = sub.SubjectID
JOIN teachers t ON m.TeacherID = t.TeacherID
WHERE s.StudentID = 1;
