from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, your account is created")
            return HttpResponseRedirect(reverse('login'))
        
    else:
        form = RegisterForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'user/profile.html')