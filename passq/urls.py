from django.urls import path,include
from . import views

urlpatterns = [
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
     path('accounts/profile/', views.index, name='home'),
    
]