from django.shortcuts import render
from django.http import HttpResponse 
from . import views  

# Create your views here.

def home(request):

    #print ('the request is', request )
    #return HttpResponse('<h1>Student IT Services - Home</h1>') 
    return render(request, 'itreporting/home.html')

def about(request): 
    return render(request, 'itreporting/home.html',{'title':'about'})

def contact(request): 
    return render(request, 'itreporting/home.html',{'title':'contact'}) 