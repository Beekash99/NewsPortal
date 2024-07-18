from django.shortcuts import render
from news.models import News

def home_page(request):
    editorial_news = News.objects.filter(is_editorial=True).order_by("-id")[:4]
    context = {
        "news":"", 
        "editorial":editorial_news,
    }
    return render(request, "index.html", context)

def contact_us(request):
  return render(request, "contactus.html")
