-- Prepares a MySQL server for the project

-- Create hbnb_test_db database if it doesn't exist or use
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create hbnb_test user if not exist or replace
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- hbnb_test should have all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- hbnb_test should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
