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
from .models import Blog_Article, Category, Tag
from .forms import Blog_Form, Category_Form, Tag_Form
import time

def categories_list(request):
    category = Category.objects.all()
    context = {
        'category' : category
    }
    return render(request, 'category_list.html', context=context)

def categories_create(request):
    form = Category_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = Category_Form()
    context = {
        'form' : form
    }
    return render(request, 'category_create.html', context=context)

def categories_update(request, id):

    category = get_object_or_404(Category_Form, id=id)

    form = Category_Form(request.POST, instance=category)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    """
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('category_list')    
    else:
        form = Blog_Form(instance=categories)
    """
    
    context = {
        'form' : form
    }

    return render(request, 'category_update.html', context=context)

def categories_delete(request, pk):

    category = get_object_or_404(Category_Form, pk=pk)

    if request.method == 'POST':
        category.delete()
        return HttpResponseRedirect("/")
    
    context = {
        'category' : category
    }
    return render(request, 'category_delete.html', context=context)

#---------------------------

def tags_list(request):
    tag = Tag.objects.all()
    context = {
        'tag' : tag
    }
    return render(request, 'tag_list.html', context=context)

def tags_create(request):
    form = Tag_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tags_list')
    else:
        form = Tag_Form()
    context = {
        'form' : form
    }
    return render(request, 'tag_create.html', context=context)

def tags_update(request, pk):

    tag = get_object_or_404(Tag_Form, pk=pk)

    form = Tag_Form(request.POST, instance=tag)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+pk)

    """
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('category_list')    
    else:
        form = Blog_Form(instance=categories)
    """
    
    context = {
        'form' : form
    }

    return render(request, 'tag_update.html', context=context)

def tags_delete(request, pk):

    tag = get_object_or_404(Tag_Form, pk=pk)

    if request.method == 'POST':
        tag.delete()
        return HttpResponseRedirect("/")
    
    context = {
        'tag' : tag
    }
    return render(request, 'tag_delete.html', context=context)

#---------------------------
def article_list(request):
    articles = Blog_Article.objects.all()
    return render(request, 'article_list.html', {'contents' : articles})

def article_detail(request, pk):
    article = Blog_Article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'content' : article})

def article_create(request):
    form = Blog_Form(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = Blog_Form()
    return render(request, 'article_form.html', {'form' : form})

def article_update(request, pk):
    article = get_object_or_404(Blog_Article, pk=pk)
    if request.method == 'POST':
        form = Blog_Form(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    elif request.method == 'GET':
        #form = article(request.GET, instance=article)
        return redirect('article_update.html')
    else:
        form = Blog_Form(instance=article)
    return render(request, 'article_detail.html', {'form' : form})

def article_delete(request, pk):
    article = get_object_or_404(Blog_Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article_delete.html', {'content' : article})








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

def article_list(request):

    articles = Blog_Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, "article_list.html", context=context)

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