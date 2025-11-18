-- Create database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user only if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;