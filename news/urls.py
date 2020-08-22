
from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, CreateArticleView, UpdateArticleView,  DeleteArticleView, CreateCategoryView, CategoryView, CategoryListView, LikeView 

urlpatterns = [
    #path('', views.home, name = "home"),
     path('', HomeView.as_view(), name = "home"),
     path('article/<int:pk>', ArticleDetailView.as_view(), name= 'article-detail'),
     path('add_article/', CreateArticleView.as_view(), name= 'add_article'),
     path('add_category/', CreateCategoryView.as_view(), name= 'add_category'),
     path('article/edit/<int:pk>', UpdateArticleView.as_view(), name= 'update_article'),
     path('article//<int:pk>/remove', DeleteArticleView.as_view(), name= 'delete_article'),
     path('category/<str:cats>/', CategoryView, name= 'category'),
     path('category-list/', CategoryListView, name= 'category-list'),
     path('like/<int:pk>', LikeView, name='like_article'),
] 


