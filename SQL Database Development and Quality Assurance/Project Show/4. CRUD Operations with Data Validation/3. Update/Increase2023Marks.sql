SELECT * FROM marks
WHERE EXTRACT(YEAR FROM ExamDate) = 2023;

UPDATE marks
SET MarkObtained = LEAST(MarkObtained + 5, 100) -- sets 100 as the max if over
WHERE EXTRACT(YEAR FROM ExamDate) = 2023;

SELECT * FROM marks
WHERE EXTRACT(YEAR FROM ExamDate) = 2023;
