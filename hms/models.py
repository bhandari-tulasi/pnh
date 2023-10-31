from django.db import models


from home.models import *
# Create your models here.
# Model for Patients Registration


class NewPatient(models.Model):
    ETHNICITY_CHOICES = [
        ("01", "Dalit"),
        ("02", "Janjati"),
        ("03", "Madhesi"),
        ("04", "Muslim"),
        ("05", "Brahmin/Chhetri"),
        ("06", "Others"),
    ]
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    SERVICE_TYPE = [
        ("1", "General"),
        ("2", "CB-IMNCI"),
        ("3", "Nutrition"),
        ("4", "Safe Motherhood"),
        ("5", "Family Planning"),
        ("6", "Tuberculosis"),
        ("7", "Leprocy"),
        ("8", "Vector Borne Disease"),
        ("9", "STI"),
        ("10", "Non Communicable Diseases"),
        ("11", "Others"),
    ]
    hospital_id = models.BigAutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ethnic_code = models.CharField(max_length=2, choices=ETHNICITY_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER)
    age = models.PositiveIntegerField()
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    service_type = models.CharField(max_length=5, choices=SERVICE_TYPE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    is_revisit = models.BooleanField(default=False)
    #registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.first_name + " " + self.last_name