-- A script that converts hbtn_0c_0 database to UTF8
USE hbtn_0c_0
ALTER DATABASE
    hbtn_0c_0
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

ALTER TABLE
    first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

ALTER TABLE
    first_table
    CHANGE name name
    VARCHAR(256)
    COLLATE utf8mb4_unicode_ci;
