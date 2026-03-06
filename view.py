from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
import jwt
import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["old_age_home_db"]
users = db["users"]

SECRET_KEY = "mysecretkey"


@api_view(['POST'])
def login_user(request):

    email = request.data.get('email')
    password = request.data.get('password')

    user = users.find_one({"email": email, "password": password})

    if not user:
        return Response({"message": "Invalid credentials"}, status=401)

    payload = {
        "user_id": str(user["_id"]),
        "email": user["email"],
        "role": user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return Response({
        "token": token,
        "role": user["role"]
    })