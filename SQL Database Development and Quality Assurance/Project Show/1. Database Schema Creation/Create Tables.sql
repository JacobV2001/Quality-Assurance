CREATE TABLE students (
    StudentID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    HomeAddress VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE teachers (
    TeacherID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    HomeAddress VARCHAR(255) NOT NULL,
    ContactNumber VARCHAR(25) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE subjects (
    SubjectID SERIAL PRIMARY KEY,
    SubjectName VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE marks (
    MarkID SERIAL PRIMARY KEY,
    StudentID INT NOT NULL,
    SubjectID INT NOT NULL,
    TeacherID INT NOT NULL DEFAULT 0,
    -- Ensure that mark is between 0 and 100
    MarkObtained INT CHECK (MarkObtained >= 0 AND MarkObtained <= 100) NOT NULL,
    ExamDate DATE NOT NULL,
    -- Foreign key prevents pairing with an ID that does not already exist
    FOREIGN KEY (StudentID) REFERENCES students(StudentID) ON DELETE CASCADE,
    FOREIGN KEY (SubjectID) REFERENCES subjects(SubjectID) ON DELETE NO ACTION,
    FOREIGN KEY (TeacherID) REFERENCES teachers(TeacherID) ON DELETE SET DEFAULT
);