import pymongo
from pymongo import ReturnDocument

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["old_age_home"]
users_collection = db["users"]
counters_collection = db["counters"]


# Ensure counter exists
if not counters_collection.find_one({"_id": "userId"}):
    counters_collection.insert_one({
        "_id": "userId",
        "seq": 0
    })


# Function to generate sequential userId
def get_next_user_id():

    counter = counters_collection.find_one_and_update(
        {"_id": "userId"},
        {"$inc": {"seq": 1}},
        return_document=ReturnDocument.AFTER
    )

    return counter["seq"]


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
    },
    {
        "email": "user@gmail.com",
        "password": "1234",
        "role": "user"
    },
    {
        "email": "dataentry@gmail.com",
        "password": "1234",
        "role": "dataentry"
    }
]


for user in users:

    existing = users_collection.find_one({"email": user["email"]})

    if not existing:

        user_id = get_next_user_id()
        user["userId"] = user_id

        users_collection.insert_one(user)

        print(f"Inserted: {user['email']} with userId {user_id}")

    else:

        # If user exists but userId missing → add it
        if "userId" not in existing:

            user_id = get_next_user_id()

            users_collection.update_one(
                {"_id": existing["_id"]},
                {"$set": {"userId": user_id}}
            )

            print(f"Updated {user['email']} with userId {user_id}")

        else:
            print(f"{user['email']} already has userId {existing['userId']}")


print("User setup completed.")