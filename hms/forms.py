from django.forms import ModelForm

from home.models import *
from . models import NewPatient


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class NewPatientForm(ModelForm):
    class Meta:
        model = NewPatient
        fields = '__all__'        