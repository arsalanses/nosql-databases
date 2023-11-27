## Docker
```sh
docker run -d --rm --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

```sh
docker exec -it redis-stack-server redis-cli
```

## SET & GET
```sh
SET user1 Moein
GET user1
```

## File
```sh
cat redis.txt | redis-cli
```

```sh
docker exec -i redis-stack-server redis-cli < redis.txt
```sh

## Namespace
```sh
keys user:*:username
```

## Array
```sh
LPUSH users:usernames Matin
RPUSH users:usernames Moeini
```

```sh
LRANGE users:usernames 0 1
```

## Hash
```sh
HSET key field value
HGETALL myhash
```

## SET
```sh
SADD user:123:favorites 347
SISMEMBER user:123:favorites 347

SADD user:123:favorites 347 121 542 100 213
SMEMBERS user:123:favorites
```
