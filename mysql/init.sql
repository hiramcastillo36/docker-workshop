CREATE DATABASE IF NOT EXISTS flaskdb;
USE flaskdb;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO tasks (description) VALUES ('Learn Docker');
INSERT INTO tasks (description) VALUES ('Build Flask Application');
INSERT INTO tasks (description) VALUES ('Connect to MySQL Database');
