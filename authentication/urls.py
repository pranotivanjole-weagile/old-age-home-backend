from django.urls import path
from .views import login_user, get_homepage_sections, get_about_page, get_services_page, get_amenities_page
from .views import save_contact_message

urlpatterns = [
    path('login/', login_user),
    path('homepage-sections/', get_homepage_sections),
    path('about/', get_about_page),
    path('services/', get_services_page),
    path('amenities/', get_amenities_page),
    path('contact/', save_contact_message),
]