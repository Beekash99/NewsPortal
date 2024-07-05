from django.db import models

class News(model.models):
  title=models.CharField(max_length=255)
  image=models.models.ImageField(upload_to="news")
  description=models.TextField()
  Created_date=models.DateTimeField(auto_now_add=True)
  updated_date=models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.title
  
  class meta():
     varbose_name='news'
     varbose_name_plural="news"
  
