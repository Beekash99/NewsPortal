from django.contrib import admin
from django.http import HttpRequest
from news.models import News, Category, ContactUs, Subscribe, SocialMedia


admin.site.site_header="NewsPortal"
admin.site.site_header="NewsPortal"
admin.site.index_title="Welcome to NewsPortal"
admin.site.app_index_template

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_date','updated_date']

    def has_add_permission(self, request) -> bool:
        return True
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ["email","created_date","updated_date"]

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','category','is_publish','created_date','updated_date']
    search_fields = ["title",]
    list_display_links  = ['title','category']
    list_filter = ["category",]

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone']

    def has_add_permission(self, request) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display=['facebook','twitter','instagram']