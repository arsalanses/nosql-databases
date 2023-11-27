import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["quera"]

print(client.list_database_names())

collection = db["users"]

print(db.list_collection_names())

danial = {"name":"danial","last_name":"keymasi","age":24}

collection.insert_one(danial)

query = collection.find({"name":"danial"})
for i in query:
    print(i)

for x in collection.find({},{ "_id": 0, "name": 1}):
    print(x)
