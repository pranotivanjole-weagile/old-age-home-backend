import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

collection = db["amenities_page"]

data = {

    "intro": {
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vestibulum commodo nibh at semper. Curabitur vel arcu nec lectus rutrum ullamcorper."
    },

    "recreation": [

        {
            "title": "Pet Therapy",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Class aptent taciti sociosqu ad litora torquent per conubia nostra."
        },

        {
            "title": "Music Therapy",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Class aptent taciti sociosqu ad litora torquent per conubia nostra."
        },

        {
            "title": "Art & Craft Therapy",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Class aptent taciti sociosqu ad litora torquent per conubia nostra."
        },

        {
            "title": "Sports Activities",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Physical activities improve mobility, confidence and overall mental well-being."
        }

    ],

    "facilities": [

        {
            "title": "Home like environment",
            "icon": "https://static.wixstatic.com/media/dd4c0b_e700498c11154527aa20638843a81f34~mv2.png"
        },

        {
            "title": "CCTV Surveillance",
            "icon": "https://static.wixstatic.com/media/dd4c0b_8e87a4bb4dad4e8fb54a0de3eae7dcb8~mv2.png"
        },

        {
            "title": "Power Back-up",
            "icon": "https://static.wixstatic.com/media/dd4c0b_0a34721c02a44f83a9220ffba634ff83~mv2.png"
        },

        {
            "title": "Highly trained caregivers",
            "icon": "https://static.wixstatic.com/media/dd4c0b_11318a485925431187b4d6316a65e7d3~mv2.png"
        },

        {
            "title": "24x7 Medical & Nursing staff",
            "icon": "https://static.wixstatic.com/media/dd4c0b_3bc9d248f0a643f48e903cc49c76fd3a~mv2.png"
        },

        {
            "title": "Walking/Jogging track",
            "icon": "https://static.wixstatic.com/media/dd4c0b_df7ecf2d516c4da682f22b66b3e7c6b3~mv2.png"
        },

        {
            "title": "Timely medical check ups",
            "icon": "https://static.wixstatic.com/media/dd4c0b_c9808b42d10e4deda529720e77828be7~mv2.png"
        },

        {
            "title": "Sports & Games",
            "icon": "https://static.wixstatic.com/media/dd4c0b_8587f40818e74d07b53094aef56d1987~mv2.png"
        },

        {
            "title": "Organic kitchen farming",
            "icon": "https://static.wixstatic.com/media/dd4c0b_07e34476058c46d8a7a1da2bc44a5987~mv2.png"
        },

        {
            "title": "Temple in Premises",
            "icon": "https://static.wixstatic.com/media/dd4c0b_e9268716501d4091b98f1233f00ef2b3~mv2.png"
        },

        {
            "title": "Recreation room with Library",
            "icon": "https://static.wixstatic.com/media/dd4c0b_a4436bd236e04ae2910661fe9ccd8cd4~mv2.png"
        },

        {
            "title": "Well equipped rooms",
            "icon": "https://static.wixstatic.com/media/dd4c0b_036e96f3ab594ffa80c51b8ac1f0da55~mv2.png"
        },

        {
            "title": "Healthy vegetarian food",
            "icon": "https://static.wixstatic.com/media/dd4c0b_5bdb1ee833a749b2a8715a9eb4f59970~mv2.png"
        },

        {
            "title": "Daily housekeeping services",
            "icon": "https://static.wixstatic.com/media/dd4c0b_5986a551fd534a968e134f8eab40cd15~mv2.png"
        }

    ]

}

collection.delete_many({})
collection.insert_one(data)

print("About page data inserted successfully")