-- a script that creates the table id_not_null on your MySQL server.
CREATE table if not exists id_not_null (`id` int default 1 , `name` varchar(256));