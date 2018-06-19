-- Loads an inital set of data into a test database.
DROP DATABASE IF EXISTS server_status;
CREATE DATABASE server_status;
USE server_status;
CREATE TABLE servers (
           id INT NOT NULL AUTO_INCREMENT,
           servername VARCHAR(255) NOT NULL,
           status VARCHAR(10) NOT NULL,
           PRIMARY KEY (id),
           UNIQUE INDEX (servername),
           UNIQUE INDEX (status)
);
INSERT INTO servers VALUES (1, "server-a", "NO-OK");
INSERT INTO servers VALUES (2, "server-b", "OK");
