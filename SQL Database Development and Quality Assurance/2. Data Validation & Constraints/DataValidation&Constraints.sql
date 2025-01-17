/*
Ensure email follows correct format
    Ensures there the minimum format has 
    -- at least one character before the @
    -- at least two characters for domain name
    -- at least 2 characters for tld
*/

ALTER TABLE students
ADD CONSTRAINT CHK_StudentEmail_Format CHECK (Email LIKE '%_@__%.__%');

ALTER TABLE teachers
ADD CONSTRAINT CHK_TeacherEmail_Format CHECK (Email LIKE '%_@__%.__%');


/*
Ensure phone numbers follow necessary formats
    Ensure has the necessary components
    -- can have 0-9, (, ), +, and space
    -- checks if it has at least 9 numbers
*/

ALTER TABLE students
ADD CONSTRAINT CHK_StudentPhoneNumber
CHECK (
    ContactNumber ~ '^[0-9\+\(\)\s\-]*$' AND
    LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) >= 10
);

ALTER TABLE teachers
ADD CONSTRAINT CHK_TeacherPhoneNumber
CHECK (
    ContactNumber ~ '^[0-9\+\(\)\s\-]*$' AND
    LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) >= 10
);

-- Ensure no dupicated marks for same student in same subject on the same day
ALTER TABLE marks
ADD CONSTRAINT UC_StudentSubject UNIQUE (StudentID, SubjectID, ExamDate);

/* Foreign Key Updates */

-- Set teacher deleted, set mark TeacherID to default 'Unassigned'
INSERT INTO teachers(TeacherID, FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES (0, 'Unassigned', 'Teacher', '2000-01-01', 'N/A', '0000000000', 'unassigned@school.com');

ALTER TABLE marks
ADD CONSTRAINT FK_TeacherDelete
FOREIGN KEY (TeacherID) REFERENCES teachers(TeacherID)
ON DELETE SET DEFAULT;
