from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Company)
admin.site.register(Visit)


class UmrahAdmin(admin.AdminSite):
    site_header= 'Umrah Dashboard'

umrah_site=UmrahAdmin(name='Umrah Dashboard')


umrah_site.register(Visit)