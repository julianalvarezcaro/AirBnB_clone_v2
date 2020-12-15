-- Creates a database and a user
-- Database: hbnb_test_db. User: hbnb_test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

SET PASSWORD FOR 'hbnb_test'@'localhost' = PASSWORD('hbnb_test_pwd');

GRANT ALL
ON hbnb_test_db . *
TO 'hbnb_test'@'localhost';

GRANT SELECT
ON performance_schema . *
TO 'hbnb_test'@'localhost';
 