from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField()
    ex_date = models.DateField()
    country = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/')
    cat_obj = models.ManyToManyField(category,blank=True)

    def __str__(self):
        return self.name



    