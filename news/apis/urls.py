from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.apis.views import NewsList, NewsCategory


router = DefaultRouter()

# api path define in routers
router.register(
    "v1/public/news", NewsList, basename="NewsList"
),
router.register(
    "v1/public/categories", NewsCategory, basename="NewsCategory"
),
urlpatterns = [
    path("", include(router.urls)),
]