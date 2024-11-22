from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
user=get_user_model() 
# Create your models here.



class CatageryModel(models.Model):
    Catagery=models.CharField(max_length=200)
    


class productModel(models.Model):
 
    catagery = models.ForeignKey(CatageryModel,on_delete=models.CASCADE)
    
    Product_name=models.CharField(max_length=200)
    Description=models.TextField()
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    Image=models.ImageField(upload_to="image/",null=True)

class CustomerModel(models.Model):

    product= models.ForeignKey(productModel,on_delete=models.CASCADE, null=True)
    customer=models.ForeignKey(user,on_delete=models.CASCADE)

    customer_name=models.CharField(max_length=100)
    customer_age=models.IntegerField()
    customer_address=models.TextField()
    customer_phone=models.CharField(max_length=10)
    Image=models.ImageField(upload_to="image/",null=True)

class cartModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(productModel,on_delete=models.CASCADE)

    product_quantity=models.PositiveIntegerField(default=1)

    def total_price(self):
        if self.product:
            return self.product_quantity * self.product.Price
        return 0

        