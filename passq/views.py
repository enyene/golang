from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import forms

from golang.settings import LOGIN_URL
from .models import ContactForm
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView,LogoutView,redirect_to_login

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin import templatetags



# Create your views here.
@user_passes_test(lambda u: Group.objects.get(name='editors') in u.groups.all()) #returns login_url if fails
@login_required #returns login_url if fails
@permission_required('contact.can comment',raise_exception=True) # returna 403 error if fails
def contact(request):

    if request.method == 'POST':
        
        form2 = ContactForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponse('form is saved to the database')
        # if form2.is_valid():
        #     form2.save()
        #     return HttpResponse('form two is saved')

            
    else:
        form2 = ContactForm()

    return render(request,'passq/contact.html',{'form':form2})


def index(request):
    if request.user.is_anonymous:
        return HttpResponse('logged in user')
    else:
        return HttpResponse('you dont have permission to view this page')

class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = LOGIN_URL
    
    redirect_authenticated_user: True

    def get_redirect_url(self):
        return reverse_lazy(index)

class LogoutView(LogoutView):
    next_page =  LOGIN_URL


class  UserSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    

