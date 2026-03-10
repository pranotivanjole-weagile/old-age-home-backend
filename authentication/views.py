from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from pymongo import MongoClient, ReturnDocument
import jwt
import datetime
import razorpay
from bson import ObjectId
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ===============================
# MongoDB Connection
# ===============================
client = MongoClient("mongodb://localhost:27017/")
db = client["old_age_home"]

users = db["users"]
homepage_sections = db["homepage_sections"]
about_page = db["about_page"]
services_page = db["services_page"]
amenities_page = db["amenities_page"]
donation_page = db["donation_page"]
donation_collection = db["donations"]
contact_messages = db["contact_messages"]
counters = db["counters"]

# ===============================
# Secret Keys
# ===============================
SECRET_KEY = "secret123"

RAZORPAY_KEY_ID = "rzp_test_7Q2abcXYZ"
RAZORPAY_KEY_SECRET = "p8ds9ds9ds9ds9ds9"

razorpay_client = razorpay.Client(
    auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)
)

# ===============================
# Generate Sequential User ID
# ===============================
def get_next_user_id():

    counter = counters.find_one_and_update(
        {"_id": "userId"},
        {"$inc": {"seq": 1}},
        return_document=ReturnDocument.AFTER
    )

    return counter["seq"]


# ===============================
# JWT Token Verification
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
# REGISTER USER
# ===============================
@api_view(['POST'])
def register_user(request):

    email = request.data.get("email")
    password = request.data.get("password")

    existing = users.find_one({"email": email})

    if existing:
        return Response({"message": "User already exists"}, status=400)

    user_id = get_next_user_id()

    user = {
        "userId": user_id,
        "email": email,
        "password": password,
        "role": "user"
    }

    users.insert_one(user)

    return Response({
        "message": "User created",
        "userId": user_id
    })


# ===============================
# LOGIN API
# ===============================
@api_view(['POST'])
def login_user(request):

    email = request.data.get("email")
    password = request.data.get("password")

    print("EMAIL:", email)
    print("PASSWORD:", password)

    user = users.find_one({"email": email})

    print("USER FOUND:", user)

    if not user or user["password"] != password:
        return Response({"message": "Invalid credentials"}, status=401)

    payload = {
        "email": user["email"],
        "role": user["role"],
        "userId": user.get("userId"),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return Response({
        "token": token,
        "role": user["role"],
        "userId": user.get("userId")
    })


# ===============================
# GET USER PROFILE
# ===============================
@api_view(['GET'])
def get_user_profile(request, user_id):

    user = users.find_one({"userId": int(user_id)}, {"password": 0})

    if not user:
        return Response({"message": "User not found"}, status=404)

    user["_id"] = str(user["_id"])

    return Response(user)


# ===============================
# HOMEPAGE API
# ===============================
@api_view(['GET'])
def get_homepage_sections(request):

    data = homepage_sections.find_one({}, {"_id": 0})

    return Response(data)


# ===============================
# ABOUT PAGE API
# ===============================
@api_view(['GET'])
def get_about_page(request):

    data = about_page.find_one({}, {"_id": 0})

    return Response(data)


# ===============================
# SERVICES PAGE API
# ===============================
@api_view(['GET'])
def get_services_page(request):

    data = services_page.find_one({}, {"_id": 0})

    return Response(data)


# ===============================
# AMENITIES PAGE API
# ===============================
@api_view(['GET'])
def get_amenities_page(request):

    data = amenities_page.find_one({}, {"_id": 0})

    return Response(data)


# ===============================
# DONATION PAGE API
# ===============================
@api_view(['GET'])
def get_donation_page(request):

    data = donation_page.find_one({}, {"_id": 0})

    return Response(data)


# ===============================
# CONTACT FORM API
# ===============================
@api_view(['POST'])
def save_contact_message(request):

    data = {
        "fullName": request.data.get("fullName"),
        "mobile": request.data.get("mobile"),
        "email": request.data.get("email"),
        "serviceType": request.data.get("serviceType"),
        "message": request.data.get("message"),
        "created_at": datetime.datetime.utcnow()
    }

    contact_messages.insert_one(data)

    return Response({
        "message": "Message saved successfully"
    })


# ===============================
# CREATE RAZORPAY ORDER
# ===============================
@api_view(['POST'])
def create_order(request):

    try:

        amount = int(request.data.get("amount", 0)) * 100

        order = razorpay_client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1
        })

        return Response({
            "orderId": order["id"],
            "key": RAZORPAY_KEY_ID
        })

    except Exception as e:

        print("CREATE ORDER ERROR:", e)

        return Response({"error": str(e)}, status=500)


# ===============================
# VERIFY RAZORPAY PAYMENT
# ===============================
@api_view(['POST'])
def verify_payment(request):

    data = request.data

    try:

        razorpay_client.utility.verify_payment_signature({
            "razorpay_order_id": data["razorpay_order_id"],
            "razorpay_payment_id": data["razorpay_payment_id"],
            "razorpay_signature": data["razorpay_signature"]
        })

        donation_collection.insert_one({
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "amount": data.get("amount"),
            "payment_id": data.get("razorpay_payment_id"),
            "created_at": datetime.datetime.utcnow()
        })

        return Response({"success": True})

    except Exception as e:

        print(e)

        return Response({"success": False})
    
   

@api_view(['POST'])
def set_language(request):
    language = request.data.get('language')
    print(language)

    return Response({"message": "Language received", "language": language})