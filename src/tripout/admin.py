from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Trip)



class TripoutAdmin(admin.AdminSite):
    site_header= 'Trip outside Dashboard'

tripout_site=TripoutAdmin(name='Trip outside Dashboard')

tripout_site.register(Trip)