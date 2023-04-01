from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import Profile
from ordering.models import Order
from .models import Category, Product
from .forms import Products,prdedit


def main(request):
    if request.method == "POST":
        se1 = request.POST.get('search')  # Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    else:
        product = Product.objects.all()
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
    else:
        user = "زائر"
    category = Category.objects.all()
    return render(request, 'main.html', {'cats': category, 'users': user, 'prd': product})


def recom(request):
    product = Product.objects.filter(recommended=True)
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
    else:
        user = "زائر"
    category = Category.objects.all()
    if request.method == "POST":
        se1 = request.POST.get('search')  # Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    return render(request, 'main.html', {'cats': category, 'users': user, 'prd': product})


def cat(request, pk):
    product = Product.objects.filter(cat_id=pk)
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
    else:
        user = "زائر"
    if request.method == "POST":
        se1 = request.POST.get('search')  # Text searching
        product = Product.objects.filter(prd_name__icontains=se1)
    category = Category.objects.all()
    return render(request, 'main.html', {'cats': category, 'users': user, 'prd': product})


def Cating(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = Profile.objects.get(user_id=request.user)
            category = Category.objects.all()
            if request.method == "POST":
                ct = request.POST.get('catname')

                newcat = Category(cat_name=ct)
                newcat.save()
                return redirect('cating')
            return render(request, 'catsmanage.html', {'cats': category, 'users': user})
        else:
            return redirect('home')
    else:
        return redirect('home')


def Prding(request):
    if request.user.is_authenticated:

        if request.user.is_staff:
            user = Profile.objects.get(user_id=request.user)
            prd = Product.objects.all()
            category = Category.objects.all()
            if request.method == "POST":
                pr = Products(data=request.POST)
                if pr.is_valid():
                    prr = pr.save(commit=False)
                    prr.img = request.FILES['img']
                    prr.sold = False
                    prr.save()
                    return redirect('prding')
            else:
                pr = Products()
            return render(request, 'prdmanage.html', {'cats': category, 'prds': prd, 'pr': pr, 'users': user})
        else:
            return redirect('home')
    else:
        return redirect('home')


def details(request, pk):


    prd = Product.objects.filter(pk=pk).first()
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
        if request.method == "POST":
            item = get_object_or_404(Product, pk=pk)
            quantity = request.POST.get('qt')

            order_qs = Order.objects.filter(user=request.user, ordered=False)
            if order_qs.exists():
                order = order_qs[0]
                # check if the order item is in the order
                if order.items.filter(name=pk).exists():
                    itt = order.items.get(name=pk)
                    itt.quantity += int(quantity)
                    itt.save()
                else:
                    order.items.create(name=item, quantity=int(quantity))
            else:
                order = Order.objects.create(user=request.user)
                order.items.create(name=item, quantity=int(quantity))
                order.save()

        return render(request, 'details.html', {'cats': category, 'pr': prd, 'users': user})
    return render(request, 'details.html', {'cats': category, 'pr': prd})


def editprd(request, pk):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = Profile.objects.get(user_id=request.user)
            prd = Product.objects.filter(pk=pk).first()
            category = Category.objects.all()

            if request.method == "POST":
                pr = prdedit(data=request.POST, instance=prd)
                if pr.is_valid():
                    prr = pr.save()
                    return redirect('details' ,pk)
            else:
                pr = prdedit(instance=prd)
            return render(request, 'editprd.html', {'cats': category, 'prds': prd, 'pr': pr, 'users': user})
        else:
            return redirect('details' ,pk)
    else:
        return redirect('details' ,pk)
