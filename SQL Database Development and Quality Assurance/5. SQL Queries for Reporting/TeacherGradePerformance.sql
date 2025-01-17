SELECT t.TeacherID, t.FirstName, t.LastName, ROUND(AVG(m.MarkObtained), 2) AS AverageMark
FROM marks m
JOIN teachers t ON m.TeacherID = t.TeacherID
GROUP BY t.TeacherID, t.FirstName, t.LastName;
