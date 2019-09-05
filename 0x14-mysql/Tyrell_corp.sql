--script for the first project
CREATE DATABASE IF NOT EXISTS tyrell_corp;
use tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
INSERT INTO `nexus6` (`id`, `name`) VALUES ("1", "Leon");
select * from nexus6;
