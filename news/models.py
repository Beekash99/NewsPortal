from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural  ="Categories"


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news_category")
    image = models.ImageField(upload_to="news")
    description = models.TextField()
    posted_by= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name="news_reporter")
    is_editorial =  models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"


class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=255)
    phone = models.PositiveBigIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"


class Comment(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Message = models.CharField(max_length=500,default='default message')

    def __str__(self):
        return "Comment"
    

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Subscribe(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class Meta:
        verbose_name = "Subcribe"
        verbose_name_plural = "Subcribes"


class SocialMedia(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return "Social Media"

    class Meta:
        verbose_name = "SocialMedia"
        verbose_name_plural = "SocialMedia"