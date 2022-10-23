from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(hall)
admin.site.register(Destination)


class WeddingAdmin(admin.AdminSite):
    site_header= 'Weddding Hall Dashboard'

wedding_site=WeddingAdmin(name='Wedding Hall Dashboard')


wedding_site.register(hall)