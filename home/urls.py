from django.urls import path
from . views import *

app_name = "home"

urlpatterns = [
    path('', home, name='home'),
    path('management', management, name='management'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('doctors', doctors, name='doctors'),
    path('download', download, name='download'),
    path('news', news, name='news'),
    path('reporting', reporting, name='reporting'),
    path('services', services, name='services'),
    path('staff', staff, name='staff'),
    path('vacancy', vacancy, name='vacancy'),
   
]