-- convert a database and tables to charset ut8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8;
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8;
