from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from blog.models import Blog_Article

#from .views import UserEditForm
from .models import CustomUser
from users.forms import CustomUserSignupForm, CustomUserChangeForm

# Create your views here.

@login_required(login_url="/users/login")
def dashboard_view(request, pk):
    user = request.user
    # Assuming pk is the user's pk and not for an article
    if user.pk != pk:
        return redirect('/users/login')

    # Get all articles authored by the user
    user_articles = Blog_Article.objects.filter(author=user)

    context = {
        'user_articles': user_articles
    }
    
    return render(request, "users:dashboard.html", context=context)

def profile_user(request, pk):

    user = get_object_or_404(CustomUser, pk=pk)

    context = {
        'user' : user
    }

    return render(request, 'users:profile_user.html', context=context)


@login_required
def delete_user(request, pk):

    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('home')  # Redirect to a success page or homepage
    
    context = {
        'user' : user
    }

    return render(request, 'users/delete_user.html', context=context)

@login_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:edit_user', pk=user.pk )  # Redirect to the user's detail page
    else:
        form = CustomUserChangeForm(instance=user)

    context = {
        'form' : form
    }

    return render(request, 'users/edit_user.html', context=context)

"""
def login_view(request):

    form = AuthenticationForm(data=request.POST)

    if request.method == "POST":
        
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("blog:article_list")
    else:
        AuthenticationForm()

    context = {
        "form" : form
    }

    return render(request, "users/login.html", context=context)

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/users/logout")
    
    return render(request, "users/logout.html")

@login_required
def delete_user(request, pk):

    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        logout(request)
        return redirect('users/logout')
    
    return render(request, 'users/delete_user.html')

@login_required
def pass_change(request):

    return render(request, 'users/pass_change.html')"""