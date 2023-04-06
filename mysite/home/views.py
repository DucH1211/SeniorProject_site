from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, FileResponse
from django.urls import reverse
from .models import Headline
from .forms import HeadlineForm
from django.conf import settings
import os

# Create your views here.

def index(request):
    
    return render(request,'home/index.html')

def srs_download(request):
    file = os.path.join(settings.BASE_DIR, 'download/SRS-Template.pdf')
    fileOpen = open(file, 'rb')
    return FileResponse(fileOpen)


def headlines(request):
    headline_list = Headline.objects.all()
    context ={
        'headline_list':headline_list,
    }
    return render(request,'home/headline.html', context)
    
def detail(request,headline_id):
    headline = Headline.objects.get(pk = headline_id)
    context = {
        'headline':headline,
    }
    return render(request,'home/detail.html',context)

def add_HL(request):
    if(request.method =='POST'):
        form = HeadlineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:headlines'))
        else:
            error_msg = "Form is invalid. Please fill in all inputs"
            return render(request,'home/HL-form.html',{ 'form':form, 'error_msg':error_msg })
    else:
        form = HeadlineForm()
    return render(request,'home/HL-form.html',{ 'form':form })

def update_HL(request,id):
    headline = Headline.objects.get(id = id)

    if(request.method =='POST'):
        form = HeadlineForm(request.POST, instance = headline)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home:detail', args=(headline.id)))
        else:
            print(form.errors)
    else:
        form = HeadlineForm()
    return render(request,'home/HL-form.html',{ 'form':form, 'headline':headline })

def delete_HL(request,id):
    headline = Headline.objects.get(id=id)
    if(request.method == 'POST'):
        headline.delete()
        return HttpResponseRedirect(reverse('home:headlines'))
    else:
        form = HeadlineForm()
    return render(request,'home/HL-delete.html',{'headline':headline })