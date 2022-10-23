from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Outside")
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="tripout/company", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.name


class Country(models.Model):
    dest = models.CharField(max_length=40,null=False)
    img=models.ImageField(upload_to="tripout/country", height_field=None, width_field=None)
    def __str__(self):
        return self.dest


class Trip(models.Model):
    comm=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
    too=models.ForeignKey(Country,on_delete=models.CASCADE,default=None)
    pic=models.ImageField(upload_to="tripout/trip", height_field=None, width_field=None)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    date = models.DateField(("المعاد"), default=datetime.date.today)
    duration=models.CharField((" مدة الرحلة"),max_length=50)
    program=models.TextField(("البرنامج"))
    kids=models.CharField((" :سياسة الاطفال"),max_length=250)
    def __str__(self):
        return self.too 
