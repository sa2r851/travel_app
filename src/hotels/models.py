from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

RATING_RANGE = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
    )
class Hotel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField((" :اسم الفندق"),max_length=50)
    imgs=models.ImageField(upload_to="hotels/", height_field=None, width_field=None, max_length=100)
    about=models.TextField((":عن الفندق"),max_length=250)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    address=models.CharField((":عنوان الفندق"),max_length=200)
    rating = models.IntegerField(choices=RATING_RANGE)
    def __str__(self):
        return self.name



class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,default=None)
    pic=models.ImageField(upload_to="hotels/room", height_field=None, width_field=None, max_length=100)
    price=models.IntegerField(('سعر الغرفة'),default=0)
    def __str__(self):
        return self.price

