SELECT m.MarkID, s.FirstName, s.LastName
FROM marks m
JOIN students s ON m.StudentID = s.studentid
WHERE MarkObtained > 100 OR MarkObtained < 0