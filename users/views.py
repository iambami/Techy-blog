from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm 
# Create your views here.

# class PasswordsChangeView(PasswordsChangeView):
#     form_class = PasswordChangeForm
#     #template_name = 'registration/change_password.html'
#     success_url = reverse_lazy('home')

# def PasswordChangeView(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, '/change_password.html', {
#         'form': form
#     })


class UserRegisterView(generic.CreateView):
    form_class =  SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class =  EditProfileForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home') 


    def get_object(self):
        return self.request.user