from django.urls import path
from accounts.views import login_page, reporter_logout
urlpatterns = [
    path('login/', login_page, name="login_page"),
    path("reporters/logout/", reporter_logout, name="logout"),
]