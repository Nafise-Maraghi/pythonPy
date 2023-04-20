from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('article/all/', AllArticlesAPIView.as_view(), name="all_articles"),
    path('search/<str:title>/', SearchArticleAPIView.as_view(), name="search"),
]
