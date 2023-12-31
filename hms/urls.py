from django.urls import path

from . views import *

app_name = "hms"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('addDepartment/', addDepartment, name='addDepartment'),
    path('addDoctors/',addDoctor, name='addDoctor'),
    path('patientRegistration/', patientRegister, name="patientRegister"),
    path('list-patients/', listPatientView, name="list-patients")
]
