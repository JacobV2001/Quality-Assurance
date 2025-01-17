SELECT sub.SubjectID, sub.SubjectName
FROM subjects sub
WHERE
    NOT EXISTS (
        SELECT 1
        FROM marks m
        WHERE m.SubjectID = sub.SubjectID
    )