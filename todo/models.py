from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    SIZE = (
        ('Small','Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large')
    )
    size = models.CharField(max_length=6, choices=SIZE,default='Large')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreated = models.DateField(auto_now_add=True)
    # dateCompleted = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=70)
    color = models.CharField(max_length=70, blank=True)
    # description = models.TextField(blank=True)
    isImportant = models.BooleanField(default=False)
    # BASKET = (
    # )
    # basket = models.CharField(max_length=10, choices= BASKET,default='Ligth Soft')

    BASKET = (
        ('Dark','Dark'),
        ('Ligth Soft', 'Ligth Soft'),
        ('Dark Soft', 'Dark Soft'),
    )
    basket = models.CharField(max_length=10, choices=BASKET,default='Ligth Soft')

    ITEMTYPE = (
        ('Shirts','Shirts'),
        ('Pants', 'Pants'),
        ('Skirts', 'Skirts'),
        ('Dresses', 'Dresses'),
        ('Shoes', 'Shoes'),
    )
    item_type = models.CharField(max_length=7, choices=ITEMTYPE,default='Shirts')

def __str__(self):
    return self.title
