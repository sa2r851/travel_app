from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Company)
admin.site.register(Moon)


class HoneymoonAdmin(admin.AdminSite):
    site_header= 'Honeymoon Dashboard'

moon_site=HoneymoonAdmin(name='Honeymoon Dashboard')


moon_site.register(Moon)