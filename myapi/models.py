from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)    
    def __str__(self):
        return self.name
# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=60,primary_key=True)
    employee_name = models.CharField(max_length=60)
    employee_salary = models.CharField(max_length=60) 
    employee_age = models.CharField(max_length=60) 
    profile_image=models.CharField(max_length=60,default=None) 
    def __str__(self):
        return self.employee_name