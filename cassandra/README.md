```sh
# docker.arvancloud.ir/
docker pull cassandra:latest
docker run -d --rm --name cassandra cassandra:latest
docker exec -it cassandra cqlsh
```

```txt
CREATE KEYSPACE IF NOT EXISTS test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
USE test;
ALTER KEYSPACE test [IF EXISTS] WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 4};
DROP KEYSPACE test;
```

```txt
CREATE TABLE keyspace test.table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
) PRIMARY KEY (partition_key_col, clustering_col1, clustering_col2) WITH comment='human-readable comment';
```

```txt
DESCRIBE table_name;
ALTER TABLE table_name ADD column datatype;
DROP TABLE table_name;
DROP TABLE IF EXISTS table_name;
TRUNCATE TABLE table_name;
```

```txt
INSERT INTO table(column1,column2,columnN)
VALUES (value1,value2,valueN);
```

```txt
INSERT INTO table(column1,column2,columnN)
VALUES 
    ('value1_1', 'value1_2', 'value1_3'),
    ('value2_1', 'value2_2', 'value2_3'),
    ('valuen_1', 'valuen_2', 'valuen_3');
```

```txt
INSERT INTO NerdMovies (movie, director, main_actor, year)
   VALUES ('Serenity', 'Joss Whedon', 'Nathan Fillion', 2005)
   USING TTL 86400;

INSERT INTO NerdMovies JSON '{"movie": "Serenity", "director": "Joss Whedon", "year": 2005}';
```
