WITH RankedStudents AS (
    SELECT m.SubjectID, sub.SubjectName, m.StudentID, s.FirstName, s.LastName, m.MarkObtained,
           ROW_NUMBER() OVER (PARTITION BY m.SubjectID ORDER BY m.MarkObtained DESC) AS Rank
    FROM marks m
    JOIN students s ON m.StudentID = s.StudentID
    JOIN subjects sub ON m.SubjectID = sub.SubjectID
)
SELECT SubjectID, SubjectName, StudentID, FirstName, LastName, MarkObtained
FROM RankedStudents
WHERE Rank <= 3
ORDER BY SubjectID, Rank;
