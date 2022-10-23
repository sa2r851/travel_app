from unicodedata import name
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

import datetime
# Create your models here.
MY_Day=(
    ('السبت','السبت'),
    ('الاحد','الاحد'),
    ('الاثنين','الاثنين'),
    ('الثلاثاء','الثلاثاء'),
    ('الاربعاء','الاربعاء'),
    ('الخميس','الخميس'),
    ('الجمعه','الجمعه'),
)

class Airport(models.Model):
    name=models.CharField((" :اسم الشركة"),max_length=50)
    def __str__(self):
        return self.name


class Aircom(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="flyin/", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.name


class Flight(models.Model):
    start=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="Start",default=None)
    end=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="End",default=None)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    date = models.DateField(("المعاد"), default=datetime.date.today)
    kids=models.CharField((" :سياسة الاطفال"),max_length=250)
    days= MultiSelectField(choices=MY_Day, max_choices=3,max_length=12)
    def __str__(self):
        return self.end

