from django.forms import ModelForm
from home.models import *

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'