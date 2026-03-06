import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

collection = db["services_page"]

data = {

    "intro": {
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vestibulum commodo nibh at semper."
    },

    "services": [

        {
            "id": "independent",
            "title": "Independent Living",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },

        {
            "id": "assisted",
            "title": "Assisted Living",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "https://static.wixstatic.com/media/dd4c0b_a7c970ad934349399130e64d8cdeaa87~mv2_d_2074_1383_s_2.jpg"
        },

        {
            "id": "postop",
            "title": "Post Operative Care",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },

        {
            "id": "palliative",
            "title": "Palliative Care",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },

        {
            "id": "maitri",
            "title": "Maitri Day Care",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },

        {
            "id": "dementia",
            "title": "Dementia Care",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },

        {
            "id": "homecare",
            "title": "Home Care",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        }

    ]
}

collection.delete_many({})
collection.insert_one(data)

print("Services page inserted successfully")