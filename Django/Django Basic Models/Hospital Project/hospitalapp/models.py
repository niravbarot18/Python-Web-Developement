from django.db import models

# Create your models here.

class Patients(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'male'), ('female', 'female')])
    phone = models.CharField(max_length=10)
    address = models.TextField()
    blood_group = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=20)
    is_admitted = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)