import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

collection = db["donation_page"]

data = {
  "header": {
    "title": "Donation",
    "subtitle": "Support our mission by making a meaningful donation today."
  },
  "cards": [
    {
      "title": "Building funds",
      "description": "Lorem ipsum dolor sit amet...",
      "price": 5000,
      "image": "assets/img/fun-activities-in-old-age-home.png"
    },
    {
      "title": "Organise Event",
      "description": "Lorem ipsum dolor sit amet...",
      "price": 7000,
      "image": "assets/img/fun-activities-in-old-age-home.png"
    },
    {
      "title": "Special meals",
      "description": "Lorem ipsum dolor sit amet...",
      "price": 7000,
      "image": "assets/img/fun-activities-in-old-age-home.png"
    }
  ]
}

collection.delete_many({})
collection.insert_one(data)

print("donation page data inserted successfully")