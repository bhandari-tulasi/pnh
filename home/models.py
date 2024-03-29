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
        return self.doctorName[:30]
    
    class Meta:
        verbose_name_plural = 'Doctors'
        


class Staff(models.Model):
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/staffs', blank=True)
    isActive = models.BooleanField(default=False)
    department=models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name[:30]




class Vacancy(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Published'),
    )
    title = models.CharField(max_length=300)
    body = models.TextField()
    status = models.CharField(max_length=10, choices = STATUS_CHOICES,
                              default='draft')
    
    # file_upload = 

