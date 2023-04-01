from django import forms
from .models import Product
from django.forms import ImageField, FileInput
class Products(forms.ModelForm):
     class Meta():
         model = Product
         fields = ('prd_name','prd_price','description','unit','recommended','cat_id')
         
         widgets = {
            'prd_name': forms.TextInput(attrs={'class': 'form-control'}),
            'prd_price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'recommended' : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'cat_id' : forms.Select(attrs={'class': 'form-control'})
        }


class prdedit(forms.ModelForm):
    class Meta():
        model = Product
        fields = ('prd_name', 'prd_price', 'description', 'unit', 'recommended', 'cat_id','img')

        widgets = {
            'prd_name': forms.TextInput(attrs={'class': 'form-control'}),
            'prd_price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'recommended': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'cat_id': forms.Select(attrs={'class': 'form-control'}),

        }