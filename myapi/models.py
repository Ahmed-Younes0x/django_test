from django.db import models

# Create your models here.
# class category(models.Model):
#     name=models.CharField(max_length=50)
#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     creation_date = models.DateField()
#     ex_date = models.DateField()
#     country = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     cat = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='static/')
#     cat_obj = models.ManyToManyField(category,blank=True)
#     # cat_obj = models.ManyToOneRel(id,category)

#     def __str__(self):
#         return self.name
    
# class ApiUser(models.Model):
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=50)
#     password=models.CharField(max_length=24)
#     email=models.EmailField()
#     dob=models.DateField()
#     phone=models.IntegerField(max_length=11)
#     last_login = models.DateTimeField(blank=True, null=True)
    
#     def __str__(self):
#         return self.name
