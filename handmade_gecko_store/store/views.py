from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ProductsForm, RegisterForm
from .models import Products, UserProfile, Basket_item
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return HttpResponse('Home page')

def orders(request):
    return HttpResponse('Orders page')

def log_out(request):

    logout(request)
    return redirect('/')

def log_in(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
        username=username,
        password=password
        )

        if user:
            login(request, user)
            return redirect('/')
        
    return render(
        request,
        'log_in.html'
    )

def catalogue(request):

    products = Products.objects.all()

    return render(
        request,
        'catalogue.html',
        {
            'products': products
        }
    )

def about_us(request):
    return HttpResponse('About page')

def my_profile(request):
    return HttpResponse('My profile page')

def our_products(request):
    return HttpResponse('Products page')

def contact_us(request):
    return HttpResponse('Contact page')

def custom_order(request):
    return HttpResponse('Custom order page')


def add_product(request):
    if request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('Home')
    else:
        form = ProductsForm()
    return render(
    request,
    'add_product.html',
    {'form': form}
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                preferred_contact=form.cleaned_data['preferred_contact']
            )

            return redirect('Log_in')

    else:
        form = RegisterForm()
    return render(
        request,
        'register.html',
        {'form': form}
        )

def basket(request):
    products = Products.objects.all()

    return render(
        request,
        'catalogue.html',
        {
            'products': products
        }
    )

@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Products, id = product_id)

    basket_item, created = Basket_item.objects.get_or_create(
        user=request.user,
        product=product)
    if not created:
        basket_item.amount += 1
        basket_item.save()
    return redirect('Catalogue')

        

