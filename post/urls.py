from django.urls import path 
from .views import getAllArticles, getArticle, creatArticle

urlpatterns = [
    path("getarticles/",getAllArticles),
    path("getarticle/<int:id>", getArticle),
    path('createarticle/',creatArticle)

]