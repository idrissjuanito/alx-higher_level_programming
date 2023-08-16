-- creates a database and a table insidei with a foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL FOREIGN KEY REFERENCES(state.id)
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (`id`)
);
