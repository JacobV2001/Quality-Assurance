SELECT StudentID AS id, ContactNumber
FROM students
WHERE ContactNumber !~ '^[0-9\+\(\)\s\-]*$' OR 
LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) < 10
UNION ALL 
SELECT TeacherID AS id, ContactNumber
FROM teachers
WHERE ContactNumber !~ '^[0-9\+\(\)\s\-]*$' OR 
LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) < 10;
