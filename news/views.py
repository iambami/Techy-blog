from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Article, Category
from .forms import ArticleForm, EditForm
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
# Create your views here.
#def home(request):
    #return render(request, 'home.html', {})
def LikeView(request, pk): 
     article = get_object_or_404(Article, id=request.POST.get('article_id'))
     liked = False
     if article.likes.filter(id=request.user.id).exists():
         article.likes.remove(request.user)
         liked = False
     else:
        article.likes.add(request.user)
        liked = True
     
     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):  
    model = Article
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id'] 

    def get_context_data(self, *args, **kwargs):
         cat_menu = Category.objects.all()
         context = super(HomeView, self).get_context_data(*args, **kwargs)
         context["cat_menu"] = cat_menu
         return context

def CategoryListView(request):
    cats_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cats_menu_list':cats_menu_list})   


 

def CategoryView(request, cats):
    category_articles = Article.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_articles':category_articles})   

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_details.html'  

    # def get_context_data(self, *args, **kwargs):
    #      cat_menu = Category.objects.all()
    #      context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    #      stuff = get_object_or_404(Article, id=self.kwargs["pk"])
    #      total_likes = stuff.total_likes()
    #      liked = False
    #      if stuff.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #      context["cat_menu"] = cat_menu
    #      context["total_likes"] = total_likes
    #      context["liked"] = liked
    #      return context

class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add_article.html'
    #fields = '__all__'

class CreateCategoryView(CreateView):
    model = Category
    #form_class = ArticleForm
    template_name = 'add_category.html'
    fields = '__all__'   

class UpdateArticleView(UpdateView):
    model = Article
    form_class = EditForm
    template_name = 'update_article.html'
    #fields = ['title', 'body']

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')




     
     