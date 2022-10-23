from django.urls import path 
from . import api
app_name='wedding'

urlpatterns = [
    path("",api.address_list_api,name='All Towns'),
    path("halls/",api.hall_list_api.as_view(),name='Filtered hall'),



]
