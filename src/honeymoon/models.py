from turtle import title
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Moon")
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="honeymoon/company", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.name

class Moon(models.Model):
    comm=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
    title=models.CharField((" :وجهه الرحلة"),max_length=150)
    pic=models.ImageField(upload_to="honeymoon/trip", height_field=None, width_field=None)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    date = models.DateField(("المعاد"), default=datetime.date.today)
    duration=models.IntegerField(('مدة الرحلة'),default=0)
    program=models.TextField(("البرنامج"))
    def __str__(self):
        return self.title

