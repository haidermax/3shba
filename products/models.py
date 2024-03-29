from django.db import models
from django.utils.text import slugify 
from datetime import datetime

class Category(models.Model):
    cat_name = models.CharField(max_length=150)
    def __str__(self):
        return self.cat_name
units=[
    ('جلسة', 'جلسة'),
    ('علبة', 'علبة'),
    ('قطعة', 'قطعة'),
    ('1غم','1غم'),
    ('5غم','5غم'),
    ('10غم','10غم'),
    ('25غم','25غم'),
    ('50','50غم'),
    ('100غم','100غم'),
    ('250غم','250غم'),
    ('500غم','500غم'),
    ('1كغم','1كغم'),
    ('100مل','100مل'),
    ('500مل','500مل'),
    ('1لتر','1 لتر'),

]
class Product(models.Model):
    prd_name = models.CharField(max_length=500, verbose_name="اسم المنتج")
    prd_price = models.IntegerField(verbose_name="السعر",default=0)
    description = models.CharField(max_length=1500,verbose_name="الوصف")
    img = models.ImageField( upload_to="media/prd/", default='media/prd/default.png', verbose_name="صورة المنتج")
    up_date = models.DateField(auto_now=False, auto_now_add=True,verbose_name="تاريخ الرفع")
    recommended = models.BooleanField(verbose_name="يعرض على الرئيسية")
    sold = models.BooleanField(verbose_name="مباع")
    unit=models.CharField(verbose_name="القياس",max_length=140,default="",choices=units)
    discount = models.IntegerField(verbose_name="الخصم", default=0)
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="القسم",null=True)
    slug = models.SlugField(verbose_name="Slug",blank=True , null=True)
    total = models.FloatField(verbose_name="السعر الكلي",default=0)
    def __str__(self):
        return self.prd_name+":"+self.cat_id.cat_name
    def save(self, *args, **kwargs):
        if self.discount>0: 
            self.total = self.prd_price-(self.prd_price * (self.discount/100))
        else:
            self.total = self.prd_price
        super(Product, self).save(*args, **kwargs)
        self.slug = "item-"+str(self.id)
        super(Product, self).save(*args, **kwargs)
    

