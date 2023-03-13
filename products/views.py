from django.shortcuts import render,redirect
from accounts.models import Profile
from .models import Category, Product
from .forms import Products


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
    if request.method == "POST":
        se1 = request.POST.get('search')    #Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    return render(request, 'main.html',{'cats':category,'users':user,'prd':product})

def cat(request,pk):
    product = Product.objects.filter(cat_id=pk)
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id= request.user)
    else:
        user="زائر"
    if request.method == "POST":
        se1 = request.POST.get('search')    #Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    category = Category.objects.all()
    return render(request, 'main.html',{'cats':category,'users':user,'prd':product})

def Cating(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            category = Category.objects.all()
            if request.method == "POST":
                ct =request.POST.get('catname')
                print(ct)
                newcat=Category(cat_name=ct)
                newcat.save()
                return redirect ('cating')
            return render(request,'catsmanage.html',{'cats':category})
        else:
            return redirect ('home')
    else:
        return redirect ('home')


def Prding(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            prd = Product.objects.all()
            if request.method == "POST":
                pr =Products(data=request.POST)
                if pr.is_valid():
                    prr=pr.save(commit=False)
                    prr.img=request.POST.get('img')
                    prr.sold=False
                    prr.save()
                    return redirect ('prding')
            else:
                pr =Products()
            return render(request,'prdmanage.html',{'prds':prd,'pr':pr})
        else:
            return redirect ('home')
    else:
        return redirect ('home')
