# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2022-01-06 11:11:50
# @Last Modified by:   Your name
# @Last Modified time: 2022-01-11 15:10:40
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        headphones = Product.objects.filter(category='H')
        return render(request,'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'headphones':headphones})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product} )

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def headphone(request, data=None):
    if data == None:
        headphones = Product.objects.filter(category='H')
    elif data == 'Boat' or data == 'Boalt' or data == 'Infinity':
        headphones = Product.objects.filter(category='H').filter(brand=data)
    elif data == 'below':
        headphones = Product.objects.filter(category='H').filter(discounted_price__lt=1000)
    elif data == 'above':
        headphones = Product.objects.filter(category='H').filter(discounted_price__gt=1000) 
    return render(request,'app/headphone.html',{'headphones':headphones})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered Successfully")
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})    

def checkout(request):
 return render(request, 'app/checkout.html')
