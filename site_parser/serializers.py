from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    """ Сериализатор модели Article """

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'created')
