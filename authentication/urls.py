from django.urls import path
from .views import (
    login_user,
    register_user,
    get_user_profile,
    get_homepage_sections,
    get_about_page,
    get_services_page,
    get_amenities_page,
    get_donation_page,
    save_contact_message,
    create_order,
    verify_payment
)
from .views import set_language

urlpatterns = [

    path('login/', login_user),
    path('register/', register_user),
    path('user/<int:user_id>/', get_user_profile),

    path('homepage-sections/', get_homepage_sections),
    path('about/', get_about_page),
    path('services/', get_services_page),
    path('amenities/', get_amenities_page),
    path('donation/', get_donation_page),

    path('contact/', save_contact_message),
    path('set-language/', set_language),
    path('create-order/', create_order),
    path('verify-payment/', verify_payment),
]