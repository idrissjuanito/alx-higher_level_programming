-- convert a database and tables to charset ut8
ALTER DATABASE CHARACTER SET utf8;
-- ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW CREATE TABLE first_table;
