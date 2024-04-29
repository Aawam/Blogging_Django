

from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              HttpResponseRedirect)
from .models import Blog_Article, Category, Tag
from .forms import Blog_Form, Category_Form, Tag_Form
import time

#----------------------------

def categories_list(request):
    category = Category.objects.all()
    context = {
        'categories' : category
    }
    return render(request, 'category_list.html', context=context)

def categories_create(request):
    form = Category_Form(request.POST)
    data = request.POST.get('title')
    category = Category.objects.filter(title=data).first()
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data['title'] == str(category):
                print("Data Duplikat")
                return redirect("categories_list")
            else:
                form.save()
            return redirect('categories_list')
    else:
        form = Category_Form()
    context = {
        'form' : form
    }
    return render(request, 'category_create.html', context=context)

def categories_update(request, pk):

    category = get_object_or_404(Category_Form, pk=pk)

    form = Category_Form(request.POST, instance=category)
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

    return render(request, 'category_update.html', context=context)

def categories_delete(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('categories_list')
    context = {
        'category' : category
    }
    return render(request, 'category_delete.html', context=context)

#---------------------------

def tags_list(request):
    tag = Tag.objects.all()
    context = {
        'tags' : tag
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


def tags_delete(request, pk):
    
    tag = get_object_or_404(Tag, pk=pk)

    if request.method == 'POST':
        tag.delete()
        return redirect("tags_delete")
    
    context = {
        'tag' : tag
    }
    return render(request, 'tags_delete.html', context=context)

#---------------------------

def article_create(request):

    if request.method == 'POST':
        form = Blog_Form(data=request.POST)

        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('article_list')

    else:
        form = Blog_Form()
    
    context = {
        'form': form
    }
    print(request.GET.get('title'))
    return render(request, 'article_create.html', context=context)

def article_list(request):
    article = Blog_Article.objects.all()
    context = {
        'contents' : article
    }
    
    return render(request, 'article_list.html', context=context)

def article_detail(request, pk):
    
    articles = get_object_or_404(Blog_Article, pk=pk)

    context = {
        'content' : articles
    }
    return render(request, 'article_detail.html', context=context)

def article_update(request, pk):

    article = get_object_or_404(Blog_Article, pk=pk)

    form = Blog_Form(request.POST, instance=article)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+pk)
    #elif request.method == 'GET':
        #form = article(request.GET, instance=article)
        #return redirect('article_update.html')

    context = {
        'form' : form
    }
    return render(request, 'article_update.html', context=context)

def article_delete(request, pk):

    article = get_object_or_404(Blog_Article, pk=pk)

    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    context = {
        'content' : article
    }
    return render(request, 'article_delete.html', context=context)



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