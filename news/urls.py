from django.urls import path
from news import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contact/", views.contact_us, name="contact_us"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("news_detail/<int:news_id>/", views.detail_news, name="detailnews"),
]