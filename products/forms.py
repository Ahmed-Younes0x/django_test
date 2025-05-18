from django import forms
from . import models

class Addproduct(forms.ModelForm):
    class Meta:
        model=models.Product
        fields='__all__'

class Update_product_Form(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    creation_date = forms.DateField()
    ex_date = forms.DateField()
    country = forms.CharField(max_length=50)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    cat = forms.CharField(max_length=50)
    image = forms.ImageField()
    
    
class AddCat(forms.Form):
    name=forms.CharField(max_length=50)