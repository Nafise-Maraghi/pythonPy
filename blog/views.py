from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class Index(TemplateView):
    def get(self, request, **kwargs):

        # getting all posts
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:10]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'summery': " ".join(article.content[3:300].split(' ')[0:-1]) + " ...",
            })
        # ____________________

        # getting all categories
        category_data = []
        all_categories = Category.objects.all()

        for category in all_categories:
            category_data.append({
                'title': category.title,
                'cover': category.cover.url,
            })
            print(category.cover.url)
            # ____________________

        context = {
            'article_data': article_data,
            'category_data': category_data,
        }

        return render(request, 'index.html', context)


class AllArticlesAPIView(APIView):

    def get(self, request):

        try:
            all_articles = Article.objects.all().order_by('-created_at')[:10]
            article_data = []

            for article in all_articles:
                article_data.append({
                    'title': article.title,
                    'cover': article.cover.url,
                    'category': article.category.title,
                    'content': article.content[3:-4]
                })

            return Response(article_data, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Internal Server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchArticleAPIView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'search.html'

    def get(self, request, title):

        try:
            article = Article.objects.filter(title__contains=title)
            serialized_data = SearchArticleSerializer(article, many=True)
            article_data = serialized_data.data

            return Response({'data': article_data}, status=status.HTTP_200_OK)

        except:
            return Response({'error': 'Internal Server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
