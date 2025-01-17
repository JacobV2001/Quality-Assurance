SELECT StudentID as ID, Email FROM students
WHERE Email NOT LIKE '%_@__%.__%'
UNION ALL
SELECT TeacherID as ID, Email FROM teachers
WHERE Email NOT LIKE '%_@__%.__%';
