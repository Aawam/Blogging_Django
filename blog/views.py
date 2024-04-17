#import pandas as pd

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

def create_view(request, test):
    articles = Blog_Article.objects.all()

    form = Blog_Form(request.POST or None)
    if form.is_valid():
        form.save
        
    context = {
        'articles' : articles,
        'form' : form,
    }    
    return render(request, 'create_view.html', context)

