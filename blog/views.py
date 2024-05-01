

from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              HttpResponseRedirect)
from .models import Blog_Article, Category, Tag
from .forms import Blog_Form, Category_Form, Tag_Form
from .templates import *
import time

#----------------------------

def categories_list(request):
    context = {}
    
    category = Category.objects.all()
    form = Category_Form()

    context['category'] = category
    
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = Category_Form(request.POST)
            else:
                category_instance = Category.objects.get(id=pk)
                form = Category_Form(request.POST, instance=category_instance)
            form.save()
            form = Category_Form()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            category = Category.objects.get(id=pk)
            category.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            category_instance = Category.objects.get(id=pk)
            form = Category_Form(instance=category_instance)

        
    context.update({'categories': category, 'form': form})

    return render(request, 'category_list.html', context=context)

#---------------------------

def tags_list(request):
    context = {}
    
    tag = Tag.objects.all()
    form = Tag_Form()

    context['tag'] = tag
    
    if request.method == 'POST':
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = Tag_Form(request.POST)
            else:
                tag_instance = Tag.objects.get(id=pk)
                form = Tag_Form(request.POST, instance=tag_instance)
            form.save()
            form = Tag_Form()

        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            tag = Tag.objects.get(id=pk)
            tag.delete()

        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            tag_instance = Tag.objects.get(id=pk)
            form = Tag_Form(instance=tag_instance)

    context.update({'tag': tag, 'form': form})

    return render(request, 'tag_list.html', context=context)

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
            return redirect("/content/"+pk)
    else:
        form=Blog_Form(instance=article)
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