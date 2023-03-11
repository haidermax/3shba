from django import forms
from .models import Profile
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfile(forms.ModelForm):
     class Meta():
         model = Profile
         fields = ('phone','img')