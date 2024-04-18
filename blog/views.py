#import pandas as pd
"""
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from blog.models import Category

from blog.models import Blog_Article
from blog.forms import Blog_Form

from core.settings import BASE_DIR

# Create your views here.

def index(request):
    # olah model
    if request.method == 'POST':
        data: dict[str, str] = {
            "nama": "awam",
            "age": 20
        }
        return JsonResponse(data)

    return render(request, 'index.html')

#def display_data(request):
    path = BASE_DIR / "out.xlsx"
    data = pd.read_excel(path)
    return JsonResponse(data.to_dict())

# Category Views
def category_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request, "index.html", context=context)
"""

from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              HttpResponseRedirect)
from .models import Blog_Article
from .forms import Blog_Form
import time

def create_view(request):
    articles = Blog_Article.objects.all()

    form = Blog_Form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success_url')
    else:
        form = Blog_Form()   
    context = {
        'articles' : articles,
        'form' : form,
    }    
    return render(request, 'create_view.html', context)

def success_view(request):
    render(request, 'success.html')
    time.sleep(3)
    return redirect('create_view')

def list_view(request):

    articles = Blog_Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, "list_view.html", context)

def detail_view(request, id):

    articles = Blog_Article.objects.get(id = id)

    context = {
        'articles' : articles,
    }

    return render(request, "detail_view.html", context)

def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Blog_Article, id = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "delete_view.html", context)