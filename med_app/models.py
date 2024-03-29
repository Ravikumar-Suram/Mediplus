from django.db import models

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'pics')
    speciality = models.CharField(max_length=30)
    designation = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self) -> str:
        return ('Dr.' + ' ' + self.name)


class Appointment(models.Model):
    pt_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.pt_name



class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    
    def __str__(self):
        return self.name