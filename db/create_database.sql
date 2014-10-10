drop database blog_db;
create database blog_db DEFAULT CHARACTER SET utf8;
grant all privileges on blog_db.* to blog@localhost identified by 'changeme' with grant option;