from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField() 
    profile_pix = models.ImageField(default= 'img.jpeg', blank= True,  null = True, upload_to= "images/profile") 
    website_url = models.CharField(max_length = 255, null=True, blank= True)
    github_url = models.CharField(max_length = 255, null=True, blank= True)
    twitter_url = models.CharField(max_length = 255, null=True, blank= True)
    linkedin_url = models.CharField(max_length = 255, null=True, blank= True)
    instagram_url = models.CharField(max_length = 255, null=True, blank= True)
    facebook_url = models.CharField(max_length = 255, null=True, blank= True)

    def __str__(self):
        return str(self.user)



class Article(models.Model):
    title = models.CharField(max_length = 255)
    artPix = models.ImageField(default= 'djan.jpg', blank = True,  null = True, upload_to= "images")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
	#date_created = models.DateTimeField(auto_now_add= True)
    post_date = models.DateField(auto_now_add=True)
    category =  models.CharField(max_length = 255, default = 'coding')
    snippet =  models.CharField(max_length = 255)
    likes = models.ManyToManyField(User, related_name='blog_post', blank=True)
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    def save(self, *args, **kwargs):
        super().save()
        