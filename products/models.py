from django.db import models

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120) #when you use a charfield you have ot use a max_length attribute.
    description     = models.TextField(blank=True, null=True)
    price           = models.DecimalField(decimal_places=2, max_digits=10000)
    summary         = models.TextField(blank=False, null=False)
    featured        = models.BooleanField()

class License(models.Model):
    rights_holder   = models.CharField(max_length=120)
    first_name      = models.CharField(max_length=120)
    last_name       = models.CharField(max_length=120)
    timeadded       = models.DateTimeField(auto_now_add=True)