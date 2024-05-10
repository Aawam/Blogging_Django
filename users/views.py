from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from blog.models import Blog_Article
from blog.views import article_list, article_detail

from .views import UserEditForm

# Create your views here.

@login_required(login_url="/users/login")
def dashboard_view(request):
    # Retrieve all articles authored by the logged-in user
    user_articles = Blog_Article.objects.filter(author=request.user)
    
    # If the user has authored at least one article, redirect to the articles page
    if not user_articles.exists():
        return redirect('/users/login/')
    
    content = {

    }
    # If the user has not authored any articles, render the dashboard template
    return render(request, "users/dashboard.html")
def register_view(request):
    
    form = UserCreationForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.save())
            return redirect("users:index")

    else:
        form = UserCreationForm()

    context = {
        "form" : form
    }

    return render(request, "users/register.html", context=context)

def login_view(request):

    form = AuthenticationForm(data=request.POST)

    if request.method == "POST":
        
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("users:index")
    else:
        AuthenticationForm()

    context = {
        "form" : form
    }

    return render(request, "users/login.html", context=context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("blog:article_list")
    
def delete_user(request, pk):
    # Get the user object
    user = User.objects.get(pk=pk)

    # Check if the logged-in user is the same as the user being deleted
    if request.user == user:
        # Delete the user
        user.delete()
        # Redirect to a success page or homepage
        return redirect('home')  # Assuming 'home' is the name of your homepage URL
    else:
        # Return a forbidden response or handle unauthorized deletion
        return render(request, 'forbidden.html', status=403)
    
def edit_user(request, pk):
    # Fetch the user object
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        # Populate the form with the user's current data
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            # Save the changes
            form.save()
            # Redirect to a success page or profile page
            return redirect('profile')  # Assuming 'profile' is the name of your profile page URL
    else:
        # Populate the form with the user's current data
        form = UserEditForm(instance=user)
    
    # Render the form
    return render(request, 'edit_user.html', {'form': form})