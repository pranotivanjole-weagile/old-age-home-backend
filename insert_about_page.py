import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

collection = db["about_page"]

data = {

    "our_story": {
        "title": "Our Story",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vestibulum commodo nibh at semper..."
    },

    "mission_vision": {
        "title": "Mission & Vision",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "image": "fun-activities-in-old-age-home.png"
    },

    "mission_points": [
        {
            "title": "Provide the continuing care for seniors",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "Provide medical assisted living",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "Maintain their independence of life",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "Create a homely environment",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "Provide the freedom they deserve",
            "image": "fun-activities-in-old-age-home.png"
        }
    ],

    "management": [
        {
            "name": "ABC XYZ",
            "designation": "Managing Chairman",
            "image": "fun-activities-in-old-age-home.png",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "name": "ABC XYZ",
            "designation": "Secretary",
            "image": "fun-activities-in-old-age-home.png",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
    ],

    "team": [
        {
            "name": "ABC XYZ",
            "designation": "Facility Supervisor",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "name": "ABC XYZ",
            "designation": "Accounts & Administration",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "name": "ABC XYZ",
            "designation": "Films & Creatives, Trustee",
            "image": "fun-activities-in-old-age-home.png"
        }
    ]
}

collection.delete_many({})
collection.insert_one(data)

print("About page data inserted successfully")