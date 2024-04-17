-- Prepares a MySQL server for the project

-- Create hbnb_dev_db database if it doesn't exist or use
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create hbnb_dev user if not exist or replace
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
