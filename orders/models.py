from django.db import models
from users.models import User
from cart.models import Cart

# Create your models here.

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('shipped','shipped'),
        ('delivered','delivered')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS,default='pending')
