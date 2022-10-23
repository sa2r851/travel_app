from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="Umrah")
    name=models.CharField((" :اسم الشركة"),max_length=50)
    logo=models.ImageField(upload_to="umrah/company", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الشركة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.name

class Visit(models.Model):
    comm=models.ForeignKey(Company,on_delete=models.CASCADE,default=None)
    hotel=models.CharField((" :الفندق "),max_length=150)
    price=models.IntegerField(('سعر العمرة'),default=0)
    date = models.DateField(("المعاد"), default=datetime.date.today)
    duration=models.IntegerField(('مدة العمرة'),default=0)
    program=models.TextField(("البرنامج"))
    def __str__(self):
        return self.hotel


