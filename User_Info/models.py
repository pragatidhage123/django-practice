from django.db import models

# Create your models here.

class Student(models.Model):

    first_name = models.CharField(max_length=255,default="unknow")
    last_name = models.CharField(max_length=200,default=True)
    address = models.CharField(max_length=150,default="unknow")
    contact_number = models.IntegerField()
    

    def __str__(self):
        return self.first_name
    

class Teacher(models.Model):

    last_name = models.CharField(max_length=150,blank=True)
    age = models.IntegerField()
    qualification = models.CharField(max_length=100,null=True)
    blood_group = models.CharField(max_length=50,default="unknow")
    married_status = models.CharField(max_length=120,null=True)
    gender = models.CharField(max_length=100,default=True)


    def __str__(self):
        return self.last_name
    



















