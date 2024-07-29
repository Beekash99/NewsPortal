from django.contrib import admin
from news.models import News, Category, ContactUs, Subcribe


admin.site.register(Category)
admin.site.register(News)
admin.site.register(ContactUs)
admin.site.register(Subcribe)