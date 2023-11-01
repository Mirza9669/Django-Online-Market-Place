from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from item.models import Item, Category
from .forms import SignUpForm, LogInForm

# Create your views here.
def index(req):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(req, 'core/index.html', {
        'items':items,
        'categories':categories
        })

def contact(req):
    return render(req, 'core/contact.html', {})

def signup(req, ):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()

            return render(req, 'core/login.html', {'form': form})
        
    else:
        form = SignUpForm()

    return render(req, 'core/signup.html', {
        'form': form,
    })

# def login(req):
#     if req.method == 'POST':
#         form = LogInForm(req.POST)
#         if form.is_valid():
#             username = req.POST['username']
#             passwd = req.POST['password']
#             user = authenticate(req, username= username, password= passwd)
#         if user is not None:
#             login()
#             return redirect('index')
#         else:
#             messages.success(req, "There was an error Logging in. Please Try Again")
#             return redirect('home')
#     else:
#         return render(req, 'login.html', {})