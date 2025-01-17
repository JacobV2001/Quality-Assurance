SELECT s.StudentID, s.FirstName, s.LastName
FROM students s
WHERE 
    NOT EXISTS (
        SELECT 1
        FROM marks m
        WHERE m.StudentID = s.StudentID
    )