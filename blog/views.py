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

def list_view(request):
    article = Blog_Article.objects.all()
    return render(request, 'blog/list_view.html', {'context' : article})

def detail_view(request, pk):
    article = Blog_Article.objects.get(pk=pk)
    return render(request, 'blog/detail_view.html', {'content' : article})

def create_article(request):
    if request.method == 'POST':
        form = Blog_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = Blog_Form()
    return render(request, 'blog/article_form.html', {'form' : form})

def update_article(request, pk):
    update = Blog_Article.get(pk=pk)
    if request.method == 'POST':
        form = Blog_Form(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = Blog_Form(instance=update)
    return render(request, 'article_form.html', {'form' : form})

def article_delete(request, pk):
    delete = Blog_Article.get(pk=pk)
    if request.method == 'POST':
        form = Blog_Form(request.POST, instance=delete)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = Blog_Form(instance=delete)
    return render(request, 'blog/article_delete.html', {'delete' : delete})


"""
def create_view(request):
    articles = Blog_Article.objects.all()

    form = Blog_Form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('success.html')
    else:
        form = Blog_Form()   
    context = {
        'articles' : articles,
        'form' : form,
    }    
    return render(request, 'create_view.html', context=context)

def success_view(request):
    render(request, 'success')
    time.sleep(3)
    return redirect('create_view.html')

def list_view(request):

    articles = Blog_Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, "list_view.html", context=context)

def detail_view(request, title):
    
    context ={}
    context["data"] = Blog_Article.objects.get(id = title)
    return render(request, "detail_view.html", context=context)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(Blog_Article, id = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/")
    
    return render(request, "delete_view.html", context)

"""