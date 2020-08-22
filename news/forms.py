from django import forms
from .models import Article, Category

#choices = [('Technoloy', '(Technoloy)'), ('Entertainment', 'Entertainment'), ('Motivation', 'Motivation')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
   choice_list.append(item)
   



class ArticleForm(forms.ModelForm):
     class Meta:
         model = Article
         fields = ('title', 'author', 'category', 'body', 'artPix')

         widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': ' ', 'id': 'oluwabamikemi', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}), 
            
         }


class EditForm(forms.ModelForm):
     class Meta:
         model = Article
         fields = ('title', 'body')

         widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
           'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
            
         }