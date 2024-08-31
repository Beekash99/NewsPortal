from rest_framework import serializers
from news.models import News, Category

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id","title","category","views_count","is_editorial", "image","description"]

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id","name",]