from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from books.models import Book



class Favorite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
