from django.shortcuts import render,HttpResponse
from .models import *



def home(request):
    emp = employee_master.objects.all()
    for x in emp:
        try:
            user = User.objects.get(employee_master=x)
            user.employee_master = x
            user.username = str(x.employee_id)
            user.save()
        except User.DoesNotExist:
            new_user = User.objects.create(username=str(x.employee_id), password='1234',employee_master=x)
    return HttpResponse('Data Created')





















