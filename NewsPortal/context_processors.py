from news.models import Category, Subscribe, SocialMedia

def category(request):
  category= Category.objects.all()
  return {
    'category':category
  }


def social(request):
    social = SocialMedia.objects.first()
    return {
        "social":social,
    }