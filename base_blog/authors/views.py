#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Authors

# Create your views here.
def authors(request):
    all_authors = Authors.objects.all().values()
    template = loader.get_template('all_authors.html')
    context = {
        'All_Authors': all_authors
    }
    return HttpResponse(template.render(context,request))