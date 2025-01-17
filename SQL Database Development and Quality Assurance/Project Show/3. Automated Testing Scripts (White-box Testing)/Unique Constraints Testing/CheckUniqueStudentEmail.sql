INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('John', 'Doe', '2000-01-01', 'Fresno, CA', '1234567890', 'studentemail@school.com');

-- Error due to needing unique student email
INSERT INTO students (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('Jane', 'Smith', '2001-01-01', 'Fresno, CA', '0987654321', 'studentemail@school.com');
