-- full permission for admin
GRANT ALL PRIVILEGES ON DATABASE sqlclass TO admin;

-- give instructor permission to manage marks (select, insert, update)
GRANT SELECT, INSERT, UPDATE ON marks TO instructor;

-- give student permission to view own marks
GRANT SELECT ON marks TO student;
GRANT SELECT ON students to student;