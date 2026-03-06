import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["old_age_home"]
collection = db["users"]

users = [
    {
        "email": "admin@gmail.com",
        "password": "1234",
        "role": "admin"
    },
    {
        "email": "superadmin@gmail.com",
        "password": "1234",
        "role": "superadmin"
    }
]

result = collection.insert_many(users)

print("Inserted IDs:", result.inserted_ids)