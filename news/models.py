from django.db import models
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
  image = models.ImageField(upload_to="news")
  description = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
  
  class Meta:
    verbose_name = 'news'
    verbose_name_plural  ="news"
  
  class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    feedback_message = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
  


