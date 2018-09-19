from django.shortcuts import render,HttpResponse, redirect, HttpResponseRedirect

from django.contrib.auth.models import User
#from django.views.generic import DetailView
from .filters import DrivingFilter
#from two_fact.mixins import TwoFactorMixin
from driveso.models import driving
#from django.core.context_processors import csrf
from django.views.decorators import csrf
from django.shortcuts import render_to_response,render,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from driveso.forms import RegistrationForm
from driveso.models import UserProfile


def home(request):
    driving_list = driving.objects.all()
    driving_filter = DrivingFilter(request.GET, queryset=driving_list)
    args={'filter': driving_filter}
    
    return render(request, 'driveso/home.html', args)
       

def profile(request):
    args={'user':request.user}
    return render(request,'driveso/profile.html',args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/driveso/home')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'driveso/register.html', args)
    

