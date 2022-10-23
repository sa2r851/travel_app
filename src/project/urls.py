"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from oneday.admin import day_site
from hotels.admin import hotel_site
from tripin.admin import tripin_site
from tripout.admin import tripout_site
from flyin.admin import fly_site
from honeymoon.admin import moon_site
from umrah.admin import umrah_site
from wedding.admin import wedding_site
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('api-auth/', include('rest_framework.urls')),
    path('flyin/', include('flyin.urls',namespace='flyin')),
    path('flyout/', include('flyout.urls',namespace='flyout')),
    path('honeymoon/', include('honeymoon.urls',namespace='honeymoon')),
    path('tripin/', include('tripin.urls',namespace='tripin')),
    path('tripout/', include('tripout.urls',namespace='tripout')),
    path('hotels/', include('hotels.urls',namespace='hotels')),
    path('oneday/', include('oneday.urls',namespace='oneday')),
    path('umrah/', include('umrah.urls',namespace='umrah')),
    path('Wedding/', include('wedding.urls',namespace='Wedding')),
    path('api-auth/', include('rest_framework.urls')),

    # company dashboard
    path("dayuse-dashboard/", day_site.urls),
    path("hotel-dashboard/", hotel_site.urls),
    path("tripin-dashboard/", tripin_site.urls),
    path("tripout-dashbord/", tripout_site.urls),
    path("flyin-dashboard/", fly_site.urls),
    path("honeymoon-dashboard/", moon_site.urls),
    path("umrah-dashboard/", umrah_site.urls),
    path("wedding-dashboard/", wedding_site.urls),









]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#admin.site.index_title=""
#admin.site.site_header=""
#admin.site.site_title=""