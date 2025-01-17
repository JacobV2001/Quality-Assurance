-- remove bob's permissions
REVOKE student FROM bob;
DROP USER bob;

-- or remove all permissions from student role
REVOKE ALL PRIVILEGES ON marks FROM student;