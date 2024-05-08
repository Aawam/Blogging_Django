from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def dashboard_view(request):
    return render(request, "users/index.html")

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
                return redirect("blog:article_list")
    else:
        AuthenticationForm()

    context = {
        "form" : form
    }

    return render(request, "users/register.html", context=context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("blog:article_list")