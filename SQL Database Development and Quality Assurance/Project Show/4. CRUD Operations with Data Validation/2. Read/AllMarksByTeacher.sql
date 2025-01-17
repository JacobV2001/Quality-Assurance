SELECT 
    t.LastName AS TeacherName, 
    sub.SubjectName, 
    s.FirstName AS StudentFirstName, 
    s.LastName AS StudentLastName,
    m.MarkObtained
FROM marks m
JOIN teachers t ON m.TeacherID = t.TeacherID
JOIN subjects sub ON m.SubjectID = sub.SubjectID
JOIN students s on m.StudentID = s.studentid
ORDER BY t.LastName, sub.SubjectName, m.MarkObtained DESC;