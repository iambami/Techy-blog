from django.urls import path
from django.conf.urls import url
from .views import UserRegisterView, UserEditView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('edit_profile', UserEditView.as_view(), name= 'edit_profile'),
    #path('password/', auth_views.PasswordChangeView, name='change_password'),
    #path('password/', auth_views.PasswordsChangeView.as_view(template_name='registration/change-password.html')),
] 