-- temp users
CREATE USER john WITH PASSWORD 'john123';
CREATE USER sarah WITH PASSWORD 'sarah123';
CREATE USER bob WITH PASSWORD 'bob123';

GRANT admin TO john;
GRANT instructor TO sarah;
GRANT student TO bob;