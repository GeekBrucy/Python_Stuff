# Python and Database
## MySQL
### Data Types
#### Number
| Type | Size | Range(singed) | Range(unsigned) |
|------|------|------|------|
| TINYIND | 1 byte | (-128, 127) | (0, 255) | 
| SMALLINT | 2 byte | (-32768, 32767) | (0, 65535) | 
| MEDIUMINT | 3 byte | (-8388608, 8388607) | (0, 16777215) | 
| INT | 4 byte | (-2147483648, 2147483647) | (0, 4294967295) | 
| BIGINT | 8 byte | (-9233372036854775808, 9233372036854775807) | (0, 18446744073709551615) | 
| FLOAT | 4 byte | (-3.402823466 E+38, 1.175494351 E-38), 0, (1.175494351 E-38, 3.402823466351 E+38) | 0, (1.175494351 E-38, 3.402823466 E+38) | 
| DOUBLE | 8 byte | | |
#### Date
| Type | Size(byte) | Format |
|------|------|------|
| DATE | 3 | YYYY-MM-DD |
| TIME | 3 | HH:MM:SS |
| YEAR | 1 | YYYY |
| DATETIME | 8 | YYYY-MM-DD HH:MM:SS |
| TIMESTAMP | 4 | YYYYMMDDHHMMSS |
#### String
| Type | Size(byte) |
|------|------|------|
| CHAR | 0 ~ 255 |
| VARCHAR | 0 ~ 65535 |
| TINYBLOB | 0 ~ 255 |
| TINYTEXT | 0 ~ 255 |
| BLOB | 0 ~ 65535 |
| TEXT | 0 ~ 65535 |
| MEDIUMBLOB | 0 ~ 16777215 |
| LONGBLOB | 0 ~ 4294967295 |
| LONGTEXT | 0 ~ 4294967295 |

#### Handle NULL Value
is null: return true if the field is null

is not null

**IMPORTANT:**Can NOT use = NULL to check, and any other value compare with NULL will always return false
### Installation (Ubuntu)
```shell
sudo apt-get install mysql-server
sudo apt install mysql-client
sudo apt install libmysqlclient-dev
```
### Check if it is installed (Ubuntu)
```shell
sudo netstat -tap | grep mysql
```

### Commands
#### Connect to MySQL
```shell
mysql -u<username> -p<password>
```
The password is not a must, because you will be prompted to enter password in next step

#### Create User
```shell
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
#### Change User Password
```shell
ALTER USER 'user'@'hostname' IDENTIFIED BY 'newPass';
```

#### Grand Privileges
```shell
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```
The asterisks in this command refer to the database and table (respectively) that they can access. For the host, use '%' to allow the connection from anywhere

#### Reload All The Privileges.
```shell
FLUSH PRIVILEGES;
```
#### Review a User’s Current Permissions
```shell
SHOW GRANTS username;
```
#### Delete a User
```shell
DROP USER ‘username’@‘localhost’;
``` 
#### Privileges List:
* ALL PRIVILEGES- as we saw previously, this would allow a MySQL user full access to a designated database (or if no database is selected, global access across the system)
* CREATE- allows them to create new tables or databases
* DROP- allows them to them to delete tables or databases
* DELETE- allows them to delete rows from tables
* INSERT- allows them to insert rows into tables
* SELECT- allows them to use the SELECT command to read through databases
* UPDATE- allow them to update table rows
* GRANT OPTION- allows them to grant or remove other users' privileges
#### Create Database
```shell
create database <DB_NAME> charset utf8;
```
#### Delete Database
```shell
drop database <DB_NAME>;
```
#### Show user create database
```shell
show create database <DB_NAME>;
```
#### Show Database
```shell
show databases;
```

#### Create Table (Basic)
```shell
create table <TABLE_NAME> (<COLUMN_NAME COLUMN_TYPE)>;
```
#### Create Table (Detail)
```shell
create table <TABLE_NAME>(
  <FIELD1> INT AUTO_INCREMENT,
  <FIELD2> CHAR(32) NOT NULL,
  <FIELD3> INT NOT NULL
  <FIELD4> DATE,
  PRIMARY KEY (<FIELD1>)
);
```

#### Insert Data
```shell
insert into <TABLE_NAME> (<FIELD1>,<FIELD2>,<FIELD3>,<FIELD4>) values (<VALUE1>, <VALUE2>, <VALUE3>, <VALUE4>)
```
#### Show Tables
```shell
use <DB_NAME>;
show tables;
```
#### Show Table Schema
```shell
desc <TABLE_NAME>;
```
or
```shell
show columns from <TABLE_NAME>
```
#### Alter Table Schema
```shell
alter table student add gender enum("m", "f");
alter table student drop gender;
alter table student modify gender enum("m", "f") not null;
alter table student change gender sex char(32) not null default "x";
```


#### Show Table Data (Basic)
```sql
select * from <TABLE_NAME>\G;
```
\G in sql is to show the data as a human readable format

#### Show Table Data (with limit and offset)
```shell
select * from <TABLE_NAME> limit 2\G;
```
get first 2 data
```shell
select * from <TABLE_NAME> limit 2 offset 1\G;
```
Ignore the first 1, show next top 2 data.
**Important:** offset must with limit

#### Update table data
```shell
update <TABLE_NAME> set <FIELD1>=<NEW-VALUE1>, <FIELD2>=<NEW-VALUE2> [where clause]
```
#### Delete table data
```shell
delete from <TABLE_NAME> where <FIELD1>=<VALUE1>;
```


#### Sort table data
```shell
select <FIELD1>,<FIELD2>,<FIELD3>,... from <TABLE_NAME> order by <FIELD1>,<FIELD2>,<FIELD3>,... [ASC [DESC]]
```

#### Group table data
```shell
select <FIELD1>,<FIELD2>,<FIELD3>,... from <TABLE_NAME> where <FIELD1> operator <VALUE1> group by <FIELD2>
```
Assume we have a table with name, age field. We would like to select all the same names and get their total age, finally we want to sum up everyone's age and display at bottom
```shell
select coalesce(name, 'Total'), sum(age) from SampleTable group by name with rollup;
```
rollup will get the total age.
coalesce will give the result of rollup a name, 'Total'

#### Foreign Key Constraints
```shell
create table student2(
  id int auto_increment,
  name char(16) not null,
  class_id int not null,
  primary key(id),
  key 'fk_class_key' (class_id),
  constraint 'fk_class_key' foreign key (class_id) references class(id)
);
```
if class table is not created or the id in class table is invalid, then the insertion of student2 table will be failed.

#### Query multiple tables
Suppose there are two tables:
|A|B|
|-|-|
|1|3|
|2|4|
|3|5|
|4|6|
##### inner join: get matching data between two tables
```shell
select * from A inner join B on A.a = B.b;
or
select A.*, B.* from A,B where A.a =B.b;
```
return:
|A|B|
|-|-|
|3|3|
|4|4|
##### left join: get all left table records, even there is no matching record in th right
```shell
select * from A left join B on A.a = B.b;
```
return:
|A|B|
|-|-|
|1|NULL|
|2|NULL|
|3|3|
|4|4|
##### right join: opposite to left join

### Transaction
* Atomicity: Only one status of one set of transaction: success or rollback
* Consistency: Rollback immediately if there is any invalide data
* Isolation: If one transaction affect others, other transactions will rollback
* Durability: InnoDB will rebuild according to the log

#### Start a transaction
```shell
begin;
# do the operation;
rollback; # if there is something wrong, and it will go back to beginning status and then finish this transaction
commit; # if everything is ok, then commit
```

### Index
#### Create Index (table already exists)
```shell
create index indexName on tableName(fieldName(length));
or
alter tableName add index [indexName] on (fieldName(length));
```
#### Create Index when creating table
```shell
create table tableName(
  id int not null auto_increment,
  username varchar(16) not null,
  index [indexName] [username(length)]
);
```
#### Delete index
```shell
drop index [indexName] on tableName;
```
#### Show index
```shell
show index from tableName;
```


### SQLAlchemy - ORM

## TODO
* Reading: http://www.cnblogs.com/wupeiqi/p/5713323.html

## My Questions
### Is it possible move a table to another database? If yes, how?