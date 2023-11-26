import redis

redis_db = redis.Redis(host="localhost", port="12121", decode_responses=True)

# SET_GET
redis_db.set("quera1","college")

res = redis_db.get("quera1")

print(res)

# HSET
value = {
    "name": "Ali",
    "surname": "Shafiee",
    "company": "QUERA",
    "age": 22
}

redis_db.hset('user', mapping=value)

res = redis_db.hgetall('user')

print(res)

# SET
redis_db.sadd("quera", "matin", "sajad", "masoud", "amin")

res = redis_db.sismember("quera", "amirali")

print(res)

redis_db.sadd("Fruits1", "Pear",  "Peach", "Guava", "Melon")
redis_db.sadd("Fruits2", "Apple", "Melon", "Berry", "Mango")
redis_db.sadd("Fruits3", "Grapes", "Banana", "Melon", "Berry")

print(redis_db.sunion("Fruits1","Fruits2","Fruits3"))

redis_db.sunionstore("Fruits","Fruits1","Fruits2","Fruits3")

res=redis_db.sdiff("Fruits1","Fruits2","Fruits3")

print(res)

redis_db.sdiffstore("difFruits","Fruits1","Fruits2","Fruits3")
