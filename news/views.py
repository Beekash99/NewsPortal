from django.shortcuts import render
from news.models import News, Category


def home_page(request):
    editorial_news = News.objects.filter(is_editorial=True).order_by("-id")[:5]
    trending_news = News.objects.all().order_by("-views_count")[:4]
    popular_news = News.objects.all().order_by("-views_count")[:4]
    recent_news = News.objects.all().order_by("-created_date")[:3]
    editor_picks= News.objects.filter(is_editorial=True).order_by("-id")[:4]
    categories = Category.objects.all()
    category_news = {
        category.name: News.objects.filter(category=category) for category in categories
        }
    context = {
    "editorial": editorial_news,
    "trending_news": trending_news,
    "popular_news": popular_news,
    "recent_news": recent_news,
    "editor_picks": editor_picks,
    "category_news":category_news,
    }
    return render(request, "index.html", context)

def category(request, category_id):
    category_related_news = News.objects.filter(category=category_id)
    context = {
        "category_related_news":category_related_news,
    }
    return render(request, "category.html", context)


def contact_us(request):
    context = {
        "from": "",
    }
    return render(request, "contactus.html", context)



def detail_news(request, news_id):
    detail_news = News.objects.get(id=news_id)
    context = {
        "detail_news":detail_news,
    }
    return render(request, "details.html", context)
