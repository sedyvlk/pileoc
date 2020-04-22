create database testdb1;
create user testadmin1 with encrypted password 'admin1';
ALTER USER testadmin1 WITH SUPERUSER;
grant all privileges on database testdb1 to testadmin1;
alter database testdb1 OWNER TO testadmin1;
create user testuser1 with encrypted password 'user1';
#GRANT CONNECT ON DATABASE testdb1 TO testuser1;
#GRANT USAGE ON SCHEMA public TO testuser1;
#GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO testuser1;
GRANT ALL PRIVILEGES ON DATABASE "testdb1" to testuser1;
\c testdb1
create table table1 (id int, name varchar(32));
insert into table1 values (1, 'Name1');
insert into table1 values (2, 'Name2');
insert into table1 values (3, 'Name3');
insert into table1 values (4, 'Name4');
