INSERT INTO teachers (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('Alice', 'Brown', '1980-05-10', '789 Maple St', '1112223333', 'teacheremail@school.com');

-- Error due to needing unique teacher email
INSERT INTO teachers (FirstName, LastName, DateOfBirth, HomeAddress, ContactNumber, Email)
VALUES ('Bob', 'Green', '1975-08-20', '101 Pine St', '4445556666', 'teacheremail@school.com'); 
