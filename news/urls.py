from django.urls import path
from news import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contact/", views.contact_us, name="contact_us"),

]