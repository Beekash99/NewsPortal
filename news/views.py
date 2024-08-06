from django.shortcuts import render, redirect 
from news.models import News, Category, Subscribe
from news.forms import ContactUsForm, SubscribeForm, AddNewsByReporterForm, updateNewsByReporterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home_page(request):
    editorial_news = News.objects.filter(is_editorial=True,is_publish=True).order_by("-id")[:5]
    trending_news = News.objects.filter(is_publish=True).order_by("-views_count")[:4]
    popular_news = News.objects.filter( is_publish=True).order_by("-views_count")[:4]
    recent_news = News.objects.filter( is_publish=True).order_by("-created_date")[:3]
    editor_picks = News.objects.filter(is_editorial=True,  is_publish=True).order_by("-id")[:4]
    categories = Category.objects.all()
    category_news = {
        category.name: News.objects.filter(category=category,  is_publish=True) for category in categories
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
    detail_news.views_count += 1
    detail_news.save()
    context = {
        "detail_news":detail_news,
    }
    return render(request, "details.html", context)

def contact_us(request):
    form = ContactUsForm(request.POST or None) #
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    return render(request, "contactus.html")

def subscribe(request):
    form = SubscribeForm(request.POST or None)
    try:
        if form.is_valid():
            form.save()
            return redirect("home_page")
        else:
            return redirect("home_page")
    except Exception as e:
        return redirect("home_page")
    return(request, "partials/footer.html")



def search(request):
    if request.method == "GET":
        query = request.GET["query"]
        search_data = News.objects.filter(title__contains=query)
        data = {
            'search_data':search_data,
        }
    else:
        return redirect("home_page")
    return render(request, "search.html", data)
    

@login_required(login_url='home_page')
def news_list(request):
    news = News.objects.filter(posted_by=request.user).order_by("-id")
    context = {
        "news":news,
    }
    return render(request, "reporter/news/list.html", context)

@login_required(login_url='home_page')
def add_news_by_reporter(request):
    context = {}
    form = AddNewsByReporterForm(request.POST, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.is_publish = False
            news.save()
            return redirect("reporter_news")
    else:
        form = AddNewsByReporterForm()
        context = {
            'form':form,
        }
        return render(request, "reporter/news/create.html", context)
    context = {
        "form":form,
    }
    return render(request, "reporter/news/create.html", context)

@login_required(login_url='home_page')
def updated_news_by_reporter(request, id):
    context = {}
    news = News.objects.get(id=id)
    form = updateNewsByReporterForm(request.POST, request.FILES, instance=news or None)
    if request.method == "POST":
        if form.is_valid():
            news = form.save(commit=False)
            news.posted_by = request.user
            news.is_publish = False
            news.save()
            return redirect("reporter_news")
    else:
        form = updateNewsByReporterForm(instance=news)
        context = {
            'form':form,
            'news':news,
        }
        return render(request, "reporter/news/update.html", context)
    context = {
        "form":form,
    }
    return render(request, "reporter/news/update.html", context)

@login_required(login_url='home_page')
def delete_news_by_reporter(request, id):
    try:
        news=News.Objects.get(id=id)
        news.delete()
        return redirect("reporter_news")
    except Exception as e:
        error_message="An error while occured while fetching the request you made"
        messages.error=(request, error_message)
        return redirect("home_page")