from django.contrib import admin
from . models import *

@admin.register(employee_master)
class employee_master_display(admin.ModelAdmin):
    list_display = ['employee_id','employee_name']

@admin.register(User)
class profile_display(admin.ModelAdmin):
    list_display = ['username','employee_master']



