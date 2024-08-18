from django.db import models

# Create your models here.


class Emp(models.Model):
    name= models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    contact= models.CharField(max_length=30)
    age= models.IntegerField()
    address= models.TextField(max_length=300)

    class Meta:
        db_table='emp'



 
from django import forms

class Empform(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'