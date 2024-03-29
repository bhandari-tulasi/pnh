from django.urls import path

from . views import *
from home.views import *

app_name = "hms"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('addDepartment/', addDepartment, name='addDepartment'),
    path('addDoctors/',addDoctor, name='addDoctor'),
    path('deleteDoctor/<int:id>}',deleteDoctor, name='deletedoctor'),
    path('patientRegistration/', patientRegister, name="patientRegister"),
    path('list-patients/', listPatientView, name="list-patients")
]
