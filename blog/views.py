from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class Index(TemplateView):
    def get(self, request, **kwargs):

        # getting all posts
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')

        if len(all_articles) > 10:
            all_articles = all_articles[:10]

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
            # ____________________

        context = {
            'article_data': article_data,
            'category_data': category_data,
        }

        return render(request, 'index.html', context)
