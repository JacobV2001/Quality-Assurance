SELECT FirstName, LastName, DateOfBirth, COUNT(*) AS DuplicateCount
FROM students
GROUP BY FirstName, LastName, DateOfBirth
HAVING COUNT(*) > 1;
