#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Authors

# Create your views here.
def authors(request):
    the_authors = Authors.objects.all().values()
    template = loader.get_template('all_authors.html')
    context = {
        'The Authors': the_authors,
    }
    return HttpResponse(template.render(context, request))