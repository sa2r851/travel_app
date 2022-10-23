
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime


# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="day-use/company", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here

    def __str__(self) :
        return self.name
class Destination(models.Model):
    dest = models.CharField(max_length=40,null=False)
    img=models.ImageField(upload_to="day-use/destination", height_field=None, width_field=None)
    def __str__(self):
        return self.dest

class fromwhere(models.Model):
    fromm = models.CharField(max_length=40,null=False)
    def __str__(self):
        return self.fromm

class day(models.Model):
        comm=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
        froom=models.ForeignKey(fromwhere,on_delete=models.CASCADE,default=None)
        too=models.ForeignKey(Destination,on_delete=models.CASCADE,default=None)
        pic=models.ImageField(upload_to="day-use/day", height_field=None, width_field=None)
        price=models.IntegerField(('سعر الرحلة'),default=0)
        date = models.DateField(("المعاد"), default=datetime.date.today)
        program=models.TextField(("البرنامج"))
        def __str__(self):
           return self.too







