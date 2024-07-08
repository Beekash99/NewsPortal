from django.db import models

class News(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to="news")
  description = models.TextField()
  Created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
  
  class meta():
    verbose_name = 'news'
    verbose_name_plural  ="news"
  
