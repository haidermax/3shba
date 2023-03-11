from django.shortcuts import render,redirect
from accounts.models import Profile
from .models import Category, Product


def main(request):
    if request.method == "POST":
        se1 = request.POST.get('search')    #Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    else:
        product = Product.objects.all()
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id= request.user)
    else:
        user="زائر"
    category = Category.objects.all()
    return render(request, 'main.html',{'cats':category,'users':user,'prd':product})

def recom(request):
    product = Product.objects.filter(recommended=True)
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id= request.user)
    else:
        user="زائر"
    category = Category.objects.all()
    return render(request, 'main.html',{'cats':category,'users':user,'prd':product})

def cat(request,pk):
    product = Product.objects.filter(cat_id=pk)
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id= request.user)
    else:
        user="زائر"
    category = Category.objects.all()
    return render(request, 'main.html',{'cats':category,'users':user,'prd':product})