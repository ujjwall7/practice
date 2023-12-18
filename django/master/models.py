from django.contrib.auth.models import AbstractUser
from django.db import models

class employee_master(models.Model):
    employee_id=models.IntegerField(null=False,primary_key=True)
    employee_name=models.CharField(max_length=100,null=True)
    
    def _str_(self):
        return (self.employee_name)
    
class User(AbstractUser):
    employee_master = models.ForeignKey(employee_master, on_delete=models.CASCADE,null=True)

#---------------------Aggregation and Annotate-------------------------

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)