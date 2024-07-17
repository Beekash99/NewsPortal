from django.shortcuts import render
from news.models import News

def home_page(request):
  news=News.objects.all() #it is query set
  context={
  "news":news,
  }
  return render(request,"index.html",context)

def contact_us(request):
  return render(request, "contactus.html")
