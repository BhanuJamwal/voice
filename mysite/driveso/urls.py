from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('register/',views.register,name='register'),
    path('home/', views.home, name='home'),
    path('login/',login,{'template_name':'driveso/login.html'},name='login'),
    path(' logout/',logout,{'template_name':'driveso/logout.html'}),
    path('profile/',views.profile,name='profile'),
    
]



