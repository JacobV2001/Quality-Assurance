SELECT t.FirstName, t.LastName
FROM teachers t
JOIN marks m ON t.TeacherID = m.teacherid
WHERE
    NOT EXISTS (
        SELECT 1 
        FROM marks m
        WHERE m.TeacherID = t.TeacherID
    )