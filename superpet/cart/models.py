from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product,through="CartItem")

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)


class Order(models.Model):
    order_id=models.CharField(primary_key=True,max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,default="")
    last_name=models.CharField(max_length=100,default="")
    phoneno=models.CharField(max_length=10,default="")
    address_line_1=models.TextField(default="")
    address_line_2=models.TextField(default="")
    city=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=50,default="")
    pincode=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,null=True,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)





