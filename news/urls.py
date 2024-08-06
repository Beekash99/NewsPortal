from django.urls import path
from news import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contact/", views.contact_us, name="contact_us"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("news_detail/<int:news_id>/", views.detail_news, name="detailnews"),
    path("subcribe/", views.subscribe, name="subcribe"),
    path("search/", views.search, name="search"),
    path("reporters/news/", views.news_list, name="reporter_news"),
    path("reporters/news/add/", views.add_news_by_reporter, name="add_news_by_reporter"),
    path("reporters/news/<int:id>/update/", views.updated_news_by_reporter, name="updated_news_by_reporter"),
    path('reporters/news/<int:id>/delete/', views.delete_news_by_reporter, name='delete_news_by_reporter'),

]