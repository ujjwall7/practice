from django.contrib.auth.models import AbstractUser
from django.db import models

class employee_master(models.Model):
    employee_id=models.IntegerField(null=False,primary_key=True)
    employee_name=models.CharField(max_length=100,null=True)
    
    def _str_(self):
        return (self.employee_name)
    
class User(AbstractUser):
    employee_master = models.ForeignKey(employee_master, on_delete=models.CASCADE,null=True)

    
