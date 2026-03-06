import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

collection = db["homepage_sections"]

data = {

    "hero_slides": [
        {
            "title": "Ageing with Joy",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "buttonText": "Know More",
            "buttonLink": "about"
        },
        {
            "title": "Comfort & Care",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "buttonText": "Explore Services",
            "buttonLink": "services"
        },
        {
            "title": "Safe & Secure",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "buttonText": "View Amenities",
            "buttonLink": "amenities"
        },
        {
            "title": "A Place Like Home",
            "image": "fun-activities-in-old-age-home.png",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "buttonText": "Contact Us",
            "buttonLink": "contact"
        }
    ],

    "who_we_are": {
        "title": "Who We Are",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet...",
        "image": "fun-activities-in-old-age-home.png",
        "buttonText": "Contact Us",
        "buttonLink": "contact"
    },

    "offerings": [
        {
            "title": "INDEPENDENT LIVING",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "ASSISTED LIVING",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "POST OPERATIVE CARE",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "DEMENTIA CARE",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "PALLIATIVE CARE",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "MAITRI DAY CARE",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        },
        {
            "title": "HOME CARE",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "image": "fun-activities-in-old-age-home.png"
        }
    ],

    "featured_on": [
        {
            "name": "Pune Mirror",
            "logo": "https://static.wixstatic.com/media/dd4c0b_748e4e83aa814a00a5d034daca46487e~mv2.png"
        },
        {
            "name": "Maharashtra Times",
            "logo": "https://static.wixstatic.com/media/dd4c0b_60e43ad8ed2b40de8ae4ba0c4adc7ff9~mv2.png"
        },
        {
            "name": "Loksatta",
            "logo": "https://static.wixstatic.com/media/dd4c0b_60ac613a37d347a18bdfa8d5e40db8da~mv2.png"
        },
        {
            "name": "Vividh Bharati",
            "logo": "https://static.wixstatic.com/media/dd4c0b_ec20bb99aa4649aa82e7da3a5ded894b~mv2.png/v1/fill/w_478,h_142,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/saptahik_default.png"
        }
    ],

    "instagram_section": {
        "title": "Join MadhurBhav",
        "subtitle": "and experience the bliss of carefree living!",
        "buttonText": "Follow Us on Instagram",
        "link": "https://www.instagram.com/madhurbhav/"
    }

}

collection.insert_one(data)
print(data)
print("Homepage data inserted successfully")