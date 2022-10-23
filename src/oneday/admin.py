from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Company)
admin.site.register(Destination)
admin.site.register(day)
admin.site.register(fromwhere)

class DayUseAdmin(admin.AdminSite):
    site_header= 'Day Use Dashboard'

day_site=DayUseAdmin(name='Day Use Dashboard')


day_site.register(day)
