#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Authors

# Create your views here.
def authors(request):
    Author = Authors.objects.all().values()
    template = loader.get_template('all_auth.html')
    context = {
        'Authors': Author,
    }
    return HttpResponse(template.render(context, request))