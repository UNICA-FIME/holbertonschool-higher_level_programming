-- creates the database hbtn_0d_2 WITH CREATE SHEMA
-- creates the user user_0d_2
--  asigned only SELECT privilege in the database 
CREATE SCHEMA IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON *.* TO user_0d_2@localhost;
