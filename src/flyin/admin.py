from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Airport)
admin.site.register(Aircom)
admin.site.register(Flight)


class FlyinAdmin(admin.AdminSite):
    site_header= 'Fly in Dashboard'

fly_site=FlyinAdmin(name='Fly in Dashboard')


fly_site.register(Flight)