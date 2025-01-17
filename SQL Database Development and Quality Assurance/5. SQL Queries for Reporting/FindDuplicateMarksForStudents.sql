SELECT m.StudentID, m.SubjectID, m.ExamDate, COUNT(*) AS DuplicateCount
FROM marks m
GROUP BY m.StudentID, m.SubjectID, m.ExamDate
HAVING COUNT(*) > 1;
