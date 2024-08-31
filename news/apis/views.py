from rest_framework import viewsets, mixins
from news.models import News, Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from news.apis.serializers import NewsSerializers, CategorySerializers


class NewsCategory(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class NewsList(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    permission_classes = [AllowAny]
    queryset = News.objects.filter(is_publish=True)
    serializer_class = NewsSerializers