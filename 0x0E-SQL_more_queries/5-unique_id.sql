-- creates a table if does not exist and make id field unique
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
