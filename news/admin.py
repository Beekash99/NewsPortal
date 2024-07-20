from django.contrib import admin
from news.models import News, Category, ContactUs


admin.site.register(Category)
admin.site.register(News)
admin.site.register(ContactUs)
