from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def indexPageView(request) :
    return render(request, 'sitepages/index.html')

def aboutPageView(request, site_name) :
    return render(request, 'sitepages/about.html')