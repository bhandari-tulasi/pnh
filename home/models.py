from django.db import models

class Department(models.Model):
    deptName = models.CharField(max_length=100)

    def __str__(self):
        return self.deptName

class Doctor(models.Model):
    doctorName = models.CharField(max_length=100)
    post = models.CharField(max_length=50)
    nmcNo = models.CharField(max_length=20)
    doctorSpecialization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    isActive = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.doctorName


class Staff(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=50)

    def __str__(self):
        return self.name



