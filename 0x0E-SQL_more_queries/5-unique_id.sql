-- script that creates the table unique_id on your MySQL server.
CREATE table if not exists unique_id (`id` int unique not null, `name` varchar(256));