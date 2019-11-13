from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hero,Employee
admin.site.register(Hero)
admin.site.register(Employee)