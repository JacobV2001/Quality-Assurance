<<<<<<< HEAD
# Project Overview
This project demonstrates the design, management, and optimization of a fully functional SQL database. 
It emphasizes key features such as data integrity, automated testing, security management, reporting, and data validation. 
The focus is on ensuring high data quality, validating functionality through automated testing, and securing access to sensitive data through role-based controls. 
Key aspects of the project include:

- **Data Integrity**: Ensuring accurate, normalization, constraints, and validation checks.
- **Automation**: Implementing automated testing for functionality and performance validation.
- **Security**: Implementing role-based security and access control.
- **Reporting and Data Analysis**: Creating complex SQL queries to extract data insights and validate database integrity.
- **Data Validation**: Using advanced SQL techniques to enforce rules and ensure clean, valid data entry.

## Table of Contents
1. [Database Design](#1-database-design)
2. [Data Validation and Constraints](#2-data-validation-and-constraints)
3. [Automated Testing Scripts](#3-automated-testing-scripts)
4. [CRUD Operations with Data Validation](#4-crud-operations-with-data-validation)
5. [Reporting Queries](#5-reporting-queries)
6. [Security and User Roles](#6-security-and-user-roles)
7. [Conclusion](#conclusion)

## 1. Database Design
The database structure reflects the organization of a real-world educational system, utilizing normalization and key constraints to ensure data integrity and efficient query performance.

### Tables and Relationships:
- **students**: StudentID, FirstName, LastName, DateOfBirth, Email, etc.
- **teachers**: TeacherID, FirstName, LastName, ContactNumber, etc.
- **subjects**: SubjectID, SubjectName
- **marks**: Marks, Foreign Keys, etc.

### Relationships:
- **One-to-many relationships**: Between students and marks, subjects and marks, and teachers and marks.
- **Many-to-many relationships**: Student enrollment in multiple subjects.

### Normalization
The database design follows a 3NF normalization to ensure data integrity and reduce redundancy.

## 2. Data Validation and Constraints
This section focuses on maintaining data accuracy and consistency through various constraints and validation rules, ensuring reliable and clean data is stored.

### Email Validation:
Ensure email addresses are formatted correctly.
```sql
ALTER TABLE students
ADD CONSTRAINT CHK_StudentEmail_Format CHECK (Email LIKE '%_@__%.__%');
```
### Phone Number Validation:
Ensure phone numbers are formatted correctly.
```sql
ALTER TABLE students
ADD CONSTRAINT CHK_StudentPhoneNumber
CHECK (
    ContactNumber ~ '^[0-9\+\(\)\s\-]*$' AND
    LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) >= 10
);
```
### Unique Marks Constraint:
Prevent duplicate marks on the same day.
```sql
ALTER TABLE marks
ADD CONSTRAINT UC_StudentSubject UNIQUE (StudentID, SubjectID, ExamDate);
```
### Foreign Key Constraints:
Ensure marks entries refence valid foreign inputs.
```sql
ALTER TABLE marks
ADD CONSTRAINT FK_TeacherDelete
FOREIGN KEY (TeacherID) REFERENCES teachers(TeacherID)
ON DELETE SET DEFAULT;
```

## 3. Automated Testing Scripts
Automated Testing is used to ensure that the database operates correctly under various inputs. The following tests were implemented:

- Constraint Testing: Ensure that uniqueness and foreign key integrity are enforced.
- Foreign Key Deletion Testing: Ensures that entries are handled correctly for ON DELETE actions.
- Data Integrity Testing: Ensure that necessary fields are populated and there are no inconsistencies.
- Unique Constraint Testing: Ensures no duplicated marks can be inserted for the same subjects on the same day.

## 4. CRUD Operations with Data Validation
The project demonstrates the ability to perform comprehensive CRUD operations while ensuring data validity:

- **Create**: Python scripts were used to automate date insertion from csv files while adhereing to constraints and validation rules.
- **Read**: SQL queries to retrieve student marks, identify average marks per subject, and detect incomplete student records.
- **Update**: Modified records of updating student marks, changing teacher assignments, and updating student contact details.
- **Delete**: Ensures proper deletions settings were followed.

## 5. Reporting Queries
Queries were developed to extract insights and to validate database integrity. This includes:

### Average Marks per Subject:
Averages grade mark per subject
```sql
SELECT SubjectName, AVG(Mark) AS AverageMarks FROM marks
JOIN subjects ON marks.SubjectID = subjects.SubjectID
GROUP BY SubjectName;
```

### Email Format Validation:
Print emails that do not follow valid format.
```sql
SELECT StudentID as ID, Email FROM students
WHERE Email NOT LIKE '%_@__%.__%'
UNION ALL
SELECT TeacherID as ID, Email FROM teachers
WHERE Email NOT LIKE '%_@__%.__%';
```

### Invalid Marks:
Print all marks outside valid range.
```sql
SELECT MarkID, StudentID, SubjectID, MarkObtained
FROM marks
WHERE MarkObtained < 0 OR MarkObtained > 100;
```

### Duplicate Marks:
Print any duplicate marks.
```sql
SELECT m.StudentID, m.SubjectID, m.ExamDate, COUNT(*) AS DuplicateCount
FROM marks m
GROUP BY m.StudentID, m.SubjectID, m.ExamDate
HAVING COUNT(*) > 1;
```

Additional queries for edge cases and data integrity checks were also implemented.

## 6. Security and User Roles
This project adds a security model using role-based access to protect data:

### Roles:
- **Admin**: Full access to all tables.
- **Instructor**: Can manage marks (select, insert, update).
- **Student**: Cam view own marks.

Example:
```sql
CREATE USER john WITH PASSWORD 'john123';
CREATE USER sarah WITH PASSWORD 'sarah123';
CREATE USER bob WITH PASSWORD 'bob123';

GRANT admin TO john;
GRANT instructor TO sarah;
GRANT student TO bob;
```

## Conclusion
This project demonstrates a comprehensive ability to design, implement, and manage a SQL database that ensures data integrity, automated testing, performance validation, and security. 
It emphasizes the creation of meaningful reports, the ability to automate testing, and the implementation of role-based security. 
The work showcases a commitment to maintaining high standards in data quality, system performance, and secure database management.
=======
# Project Overview
This project demonstrates the design, management, and optimization of a fully functional SQL database. 
It emphasizes key features such as data integrity, automated testing, security management, reporting, and data validation. 
The focus is on ensuring high data quality, validating functionality through automated testing, and securing access to sensitive data through role-based controls. 
Key aspects of the project include:

- **Data Integrity**: Ensuring accurate, normalization, constraints, and validation checks.
- **Automation**: Implementing automated testing for functionality and performance validation.
- **Security**: Implementing role-based security and access control.
- **Reporting and Data Analysis**: Creating complex SQL queries to extract data insights and validate database integrity.
- **Data Validation**: Using advanced SQL techniques to enforce rules and ensure clean, valid data entry.

## Table of Contents
1. [Database Design](#1-database-design)
2. [Data Validation and Constraints](#2-data-validation-and-constraints)
3. [Automated Testing Scripts](#3-automated-testing-scripts)
4. [CRUD Operations with Data Validation](#4-crud-operations-with-data-validation)
5. [Reporting Queries](#5-reporting-queries)
6. [Security and User Roles](#6-security-and-user-roles)
7. [Conclusion](#conclusion)

## 1. Database Design
The database structure reflects the organization of a real-world educational system, utilizing normalization and key constraints to ensure data integrity and efficient query performance.

### Tables and Relationships:
- **students**: StudentID, FirstName, LastName, DateOfBirth, Email, etc.
- **teachers**: TeacherID, FirstName, LastName, ContactNumber, etc.
- **subjects**: SubjectID, SubjectName
- **marks**: Marks, Foreign Keys, etc.

### Relationships:
- **One-to-many relationships**: Between students and marks, subjects and marks, and teachers and marks.
- **Many-to-many relationships**: Student enrollment in multiple subjects.

### Normalization
The database design follows a 3NF normalization to ensure data integrity and reduce redundancy.

## 2. Data Validation and Constraints
This section focuses on maintaining data accuracy and consistency through various constraints and validation rules, ensuring reliable and clean data is stored.

### Email Validation:
Ensure email addresses are formatted correctly.
```sql
ALTER TABLE students
ADD CONSTRAINT CHK_StudentEmail_Format CHECK (Email LIKE '%_@__%.__%');
```
### Phone Number Validation:
Ensure phone numbers are formatted correctly.
```sql
ALTER TABLE students
ADD CONSTRAINT CHK_StudentPhoneNumber
CHECK (
    ContactNumber ~ '^[0-9\+\(\)\s\-]*$' AND
    LENGTH(REGEXP_REPLACE(ContactNumber, '[^0-9]', '', 'g')) >= 10
);
```
### Unique Marks Constraint:
Prevent duplicate marks on the same day.
```sql
ALTER TABLE marks
ADD CONSTRAINT UC_StudentSubject UNIQUE (StudentID, SubjectID, ExamDate);
```
### Foreign Key Constraints:
Ensure marks entries refence valid foreign inputs.
```sql
ALTER TABLE marks
ADD CONSTRAINT FK_TeacherDelete
FOREIGN KEY (TeacherID) REFERENCES teachers(TeacherID)
ON DELETE SET DEFAULT;
```

## 3. Automated Testing Scripts
Automated Testing is used to ensure that the database operates correctly under various inputs. The following tests were implemented:

- Constraint Testing: Ensure that uniqueness and foreign key integrity are enforced.
- Foreign Key Deletion Testing: Ensures that entries are handled correctly for ON DELETE actions.
- Data Integrity Testing: Ensure that necessary fields are populated and there are no inconsistencies.
- Unique Constraint Testing: Ensures no duplicated marks can be inserted for the same subjects on the same day.

## 4. CRUD Operations with Data Validation
The project demonstrates the ability to perform comprehensive CRUD operations while ensuring data validity:

- **Create**: Python scripts were used to automate date insertion from csv files while adhereing to constraints and validation rules.
- **Read**: SQL queries to retrieve student marks, identify average marks per subject, and detect incomplete student records.
- **Update**: Modified records of updating student marks, changing teacher assignments, and updating student contact details.
- **Delete**: Ensures proper deletions settings were followed.

## 5. Reporting Queries
Queries were developed to extract insights and to validate database integrity. This includes:

### Average Marks per Subject:
Averages grade mark per subject
```sql
SELECT SubjectName, AVG(Mark) AS AverageMarks FROM marks
JOIN subjects ON marks.SubjectID = subjects.SubjectID
GROUP BY SubjectName;
```

### Email Format Validation:
Print emails that do not follow valid format.
```sql
SELECT StudentID as ID, Email FROM students
WHERE Email NOT LIKE '%_@__%.__%'
UNION ALL
SELECT TeacherID as ID, Email FROM teachers
WHERE Email NOT LIKE '%_@__%.__%';
```

### Invalid Marks:
Print all marks outside valid range.
```sql
SELECT MarkID, StudentID, SubjectID, MarkObtained
FROM marks
WHERE MarkObtained < 0 OR MarkObtained > 100;
```

### Duplicate Marks:
Print any duplicate marks.
```sql
SELECT m.StudentID, m.SubjectID, m.ExamDate, COUNT(*) AS DuplicateCount
FROM marks m
GROUP BY m.StudentID, m.SubjectID, m.ExamDate
HAVING COUNT(*) > 1;
```

Additional queries for edge cases and data integrity checks were also implemented.

## 6. Security and User Roles
This project adds a security model using role-based access to protect data:

### Roles:
- **Admin**: Full access to all tables.
- **Instructor**: Can manage marks (select, insert, update).
- **Student**: Cam view own marks.

Example:
```sql
CREATE USER john WITH PASSWORD 'john123';
CREATE USER sarah WITH PASSWORD 'sarah123';
CREATE USER bob WITH PASSWORD 'bob123';

GRANT admin TO john;
GRANT instructor TO sarah;
GRANT student TO bob;
```

## Conclusion
This project demonstrates a comprehensive ability to design, implement, and manage a SQL database that ensures data integrity, automated testing, performance validation, and security. 
It emphasizes the creation of meaningful reports, the ability to automate testing, and the implementation of role-based security. 
The work showcases a commitment to maintaining high standards in data quality, system performance, and secure database management.
>>>>>>> 67d10dfef01353a0fa3bb05cd751a689bc205503
