from django.contrib import admin
from . models import *

@admin.register(employee_master)
class employee_master_display(admin.ModelAdmin):
    list_display = ['employee_id','employee_name']

@admin.register(User)
class profile_display(admin.ModelAdmin):
    list_display = ['username','employee_master']

@admin.register(Author)
class profile_display(admin.ModelAdmin):
    list_display = ('name', 'age', )

@admin.register(Publisher)
class profile_display(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Book)
class profile_display(admin.ModelAdmin):
    list_display = ('name', 'pages', 'price', 'rating', 'publisher', 'pubdate', )

@admin.register(Store)
class profile_display(admin.ModelAdmin):
    list_display = ['name']



