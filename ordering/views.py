from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
from .models import Order, Items
from accounts.models import Profile
from products.models import Category
from django.utils import timezone


def delitem(request, pk):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    items = order.items.filter(pk=pk)
    for i in items:
        i.delete()
        return redirect("myorder")


def ordering(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(name=pk).exists():
            itt = order.items.get(name=pk)
            itt.quantity += 1
            itt.save()
        else:

            order.items.create(name=item, quantity=1)
    else:
        order = Order.objects.create(
            user=request.user)
        order.items.create(name=item, quantity=1)
    return redirect('home')


def myorder(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id=request.user)
    else:
        user = "زائر"
    order = Order.objects.filter(user=request.user, ordered=False)
    if order.exists():
        total = order[0].get_total()
        itt = order[0].items.all()
        return render(request, "myorders.html", {'users': user, 'order': itt, 'total': total, 'cats': category})
    else:
        return render(request, "myorders.html", {'users': user, 'cats': category})


def DeleteOrder(request):
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs[0]
    items = order.items.all()
    for i in items:
        i.delete()
    order.delete()
    return redirect("myorder")


def SendOrder(request):
    order = get_object_or_404(Order, user=request.user, ordered=False)
    order.ordered = True
    order.ordered_date = timezone.datetime.today()
    order.save()
    return redirect('myorder')
