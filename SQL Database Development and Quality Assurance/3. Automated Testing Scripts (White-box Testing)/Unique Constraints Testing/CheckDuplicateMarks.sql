INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate)
VALUES (1, 1, 1, 85, '2025-01-01');

-- Error due to necessary unique (StudentID, SubjectID, and ExamDate)
INSERT INTO marks (StudentID, SubjectID, TeacherID, MarkObtained, ExamDate)
VALUES (1, 1, 2, 90, '2025-01-01');
