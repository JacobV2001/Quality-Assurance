SELECT sub.SubjectName, ROUND(AVG(m.MarkObtained), 2) AS AverageMark
FROM marks m
JOIN subjects sub ON m.SubjectID = sub.SubjectID
GROUP BY sub.SubjectName;
