-- creates a table if does not exist and make id field unique
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
