from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Items(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.name.prd_name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)
    ordered_date = models.DateField(auto_now=True)
    ordered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} of {self.ordered_date}"
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.name.total*order_item.quantity
        return total