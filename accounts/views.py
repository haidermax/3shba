from django.shortcuts import render,redirect
from .forms import UserForm,UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Profile,User
from products.models import Category
msg=""
def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
def register(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        category = Category.objects.all()
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form = UserProfile(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user_id = user
                profile.img = request.FILES['img']
                profile.save()
                registered = True
                return redirect('home')
            else:
                print(user_form.errors,profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfile()
        return render(request,'registration.html',
                            {'cats':category,'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})
def user_login(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        category = Category.objects.all()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                msg="خطأ في الدخول! يرجى التأكد من المعلومات"
                return render(request, 'login.html', {'msg':msg})
        else:
            return render(request, 'login.html', {'cats':category})

def myinfo(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        user = Profile.objects.get(user_id= request.user)
    else:
        user="زائر"
    user = Profile.objects.get(user_id=request.user)
    return render(request, "myinfo.html",{'cats':category,'users':user,'user':user})