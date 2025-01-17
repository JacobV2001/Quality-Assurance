SELECT 
    CASE
        WHEN MarkObtained BETWEEN 0 AND 39 THEN '0-39'
        WHEN MarkObtained BETWEEN 40 AND 59 THEN '40-59'
        WHEN MarkObtained BETWEEN 60 AND 79 THEN '60-79'
        WHEN MarkObtained BETWEEN 80 AND 100 THEN '80-100'
    END AS MarkRange,
    COUNT(*) AS Count
FROM marks
GROUP BY MarkRange;
