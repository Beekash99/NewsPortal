from news.models import Category, Subcribe

def category(request):
  category= Category.objects.all()
  return {
    'category':category
  }