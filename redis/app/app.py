import redis
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.json.path import Path

from redis.commands.search.query import Query


redis_db=redis.Redis(host="localhost", port=12121, decode_responses=True)

user1 = {
    "user": {
        "name": "Paul John",
        "email": "paul.john@example.com",
        "age": 42,
        "city": "London"
    }
}
user2 = {
    "user": {
        "name": "Eden Zamir",
        "email": "eden.zamir@example.com",
        "age": 29,
        "city": "Tel Aviv"
    }
}
user3 = {
    "user": {
        "name": "Paul Zamir",
        "email": "paul.zamir@example.com",
        "age": 35,
        "city": "Tel Aviv"
    }
}

schema = (
    TextField("$.user.name", as_name="name"),
    TagField("$.user.city", as_name="city"),
    NumericField("$.user.age", as_name="age")
)

redis_db.ft("idx:users").create_index(
    schema,
    definition=IndexDefinition(
        prefix=["user:"],
        index_type=IndexType.JSON
    )
)

redis_db.json().set(name="user:1", path=Path.root_path(), obj=user1)
redis_db.json().set(name="user:2", path=Path.root_path(), obj=user2)
redis_db.json().set(name="user:3", path=Path.root_path(), obj=user3)

res = redis_db.ft("idx:users").search("Paul")
print(res)

res = redis_db.ft("idx:users").search(Query("@age:[20 40]"))
print(res)

res = redis_db.ft("idx:users").search(Query("Paul @age:[20 40]"))
print(res)

res = redis_db.ft("idx:users").search(Query("@city:{London}"))
print(res)

res = redis_db.ft("idx:users").search(Query("@city:{London | Tel Aviv}"))
print(res)
