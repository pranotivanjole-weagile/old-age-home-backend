from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from pymongo import MongoClient
import jwt
import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

users = db["users"]
homepage_sections = db["homepage_sections"]
about_page = db["about_page"]  
services_page = db ["services_page"]
amenities_page = db ["amenities_page"]


SECRET_KEY = "secret123"


# ===============================
# JWT Authentication Function
# ===============================
def verify_token(request):

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise AuthenticationFailed("Token missing")

    try:
        token = auth_header.split(" ")[1]
    except IndexError:
        raise AuthenticationFailed("Invalid token format")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Token expired")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Invalid token")

    return payload


# ===============================
# Login API
# ===============================
@api_view(['POST'])
def login_user(request):

    email = request.data.get('email')
    password = request.data.get('password')

    user = users.find_one({
        "email": email,
        "password": password
    })

    if not user:
        return Response({"message": "Invalid credentials"}, status=401)

    payload = {
        "email": user["email"],
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return Response({
        "token": token,
        "role": user["role"]
    })


# ===============================
# Public Homepage API
# ===============================
@api_view(['GET'])
def get_homepage_sections(request):

    data = homepage_sections.find_one({}, {"_id": 0})

    return Response(data)
# ===============================
# About Page API
# ===============================
@api_view(['GET'])
def get_about_page(request):

    data = about_page.find_one({}, {"_id": 0})

    return Response(data)

# ===============================
# services Page API
# ===============================
@api_view(['GET'])
def get_services_page(request):

    data = services_page.find_one({}, {"_id": 0})

    return Response(data)

# ===============================
# amenities Page API
# ===============================
@api_view(['GET'])
def get_amenities_page(request):

    data = amenities_page.find_one({}, {"_id": 0})

    return Response(data)

# ===============================
# Contact Form API
# ===============================

contact_messages = db["contact_messages"]

@api_view(['POST'])
def save_contact_message(request):

    data = {
        "fullName": request.data.get("fullName"),
        "mobile": request.data.get("mobile"),
        "email": request.data.get("email"),
        "serviceType": request.data.get("serviceType"),
        "message": request.data.get("message")
    }

    contact_messages.insert_one(data)

    return Response({
        "message": "Message saved successfully"
    })