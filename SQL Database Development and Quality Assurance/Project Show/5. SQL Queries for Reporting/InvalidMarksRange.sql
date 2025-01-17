SELECT MarkID, StudentID, SubjectID, MarkObtained
FROM marks
WHERE MarkObtained < 0 OR MarkObtained > 100;
