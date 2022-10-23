from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Inside")
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="tripin/company", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.name


class Destination(models.Model):
    dest = models.CharField(max_length=40,null=False)
    img=models.ImageField(upload_to="tripin/destination", height_field=None, width_field=None)
    def __str__(self):
        return self.dest


class Tour(models.Model):
    comm=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
    too=models.ForeignKey(Destination,on_delete=models.CASCADE,default=None)
    pic=models.ImageField(upload_to="tripin/tour", height_field=None, width_field=None)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    date = models.DateField(("المعاد"), default=datetime.date.today)
    duration=models.CharField((" مدة الرحلة"),max_length=50)
    program=models.TextField(("البرنامج"))
    kids=models.CharField((" :سياسة الاطفال"),max_length=250)
    def __str__(self):
        return self.too
