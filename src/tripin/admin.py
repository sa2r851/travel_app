from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Company)
admin.site.register(Destination)
admin.site.register(Tour)


class TripinAdmin(admin.AdminSite):
    site_header= 'Trip inside Dashboard'

tripin_site=TripinAdmin(name='Trip inside Dashboard')


tripin_site.register(Tour)