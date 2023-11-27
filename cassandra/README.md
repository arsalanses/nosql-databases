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
