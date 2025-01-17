With HighestMarkPerSubject AS (
    SELECT
        sub.SubjectName,
        MAX(m.MarkObtained) AS HighestMark
    FROM marks m
    JOIN subjects sub ON m.SubjectID = sub.SubjectID
    GROUP BY sub.SubjectName
),
TopStudents AS (
    SELECT
        h.SubjectName,
        s.FirstName,
        s.LastName,
        h.HighestMark
    FROM HighestMarkPerSubject h
    JOIN subjects sub ON h.SubjectName = sub.SubjectName
    JOIN marks m ON sub.SubjectID = m.SubjectID AND h.HighestMark = m.MarkObtained
    JOIN students s ON m.StudentID = s.StudentID
)
SELECT SubjectName, FirstName, LastName, HighestMark
FROM TopStudents
ORDER BY SubjectName, HighestMark DESC;