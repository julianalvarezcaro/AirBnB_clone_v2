-- Creates a database and a user
-- Database: hbnb_dev_db. User: hbnb_dev
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

SET PASSWORD FOR 'hbnb_dev'@'localhost' = PASSWORD('hbnb_dev_pwd');

GRANT ALL
ON hbnb_dev_db . *
TO 'hbnb_dev'@'localhost';

GRANT SELECT
ON performance_schema . *
TO 'hbnb_dev'@'localhost';
