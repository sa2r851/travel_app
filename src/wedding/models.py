from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
class Destination(models.Model):
    dest = models.CharField(max_length=40,null=False)
    img=models.ImageField(upload_to="wedding/destination", height_field=None, width_field=None)
    def __str__(self):
        return self.dest

class hall(models.Model):
    name=models.CharField((" :اسم القاعة"),max_length=50)
    imgs=models.ImageField(upload_to="wedding/hall", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن القاعة"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    price=models.IntegerField(('سعر القاعة'),default=0)
    number=models.IntegerField(('عدد الافراد '),default=0)
    address=models.CharField((" :اسم القاعة"),max_length=50)
    optionss=models.TextField((": الاضافات"),max_length=250)
    location=models.ForeignKey(Destination,on_delete=models.CASCADE,default=None)
    program=models.TextField((":برنامج الفرح "),max_length=250)
    def __str__(self):
        return self.name



# price - number - dest - 