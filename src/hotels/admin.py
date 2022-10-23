from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Room)
admin.site.register(Hotel)



class HotelAdmin(admin.AdminSite):
    site_header= 'Hotel Dashboard'

hotel_site=HotelAdmin(name='Hotels Dashboard')


hotel_site.register(Room)