-- making a replica user and updating permissions
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'eyes';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'
GRANT ALL ON `mysql`.* TO 'holberton_user'@'localhost';


mysql -uholberton_user -p -e 'SELECT user, replica_user FROM mysql.user'
