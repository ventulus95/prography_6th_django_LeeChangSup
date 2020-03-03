from .models import Article
from rest_framework import serializers,viewsets

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields =  '__all__'

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer