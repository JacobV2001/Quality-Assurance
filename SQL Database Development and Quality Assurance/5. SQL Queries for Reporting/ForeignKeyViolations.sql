=SELECT s.StudentID, sub.SubjectID, t.TeacherID 
FROM marks m
LEFT JOIN students s ON m.StudentID = s.StudentID
LEFT JOIN subjects sub ON m.SubjectID = sub.SubjectID
LEFT JOIN teachers t ON m.TeacherID = t.TeacherID
WHERE s.StudentID IS NULL -- no student
OR sub.SubjectID IS NULL -- no subject
OR (t.TeacherID IS NULL AND t.TeacherID != 0); -- no teacher and not default teacher