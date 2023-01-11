from django.db import models
from django.contrib.auth.models import User
from appointments.models import models

# Create your models here.

"""class CustomGroup(Group):
    users = models.ManyToManyField(User, related_name='custom_groups')
"""

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True,)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  
    diagnosis = models.CharField(max_length=200,null=True, blank=True,)
    doctors = models.ManyToManyField(User, related_name='medics')
    medical_history = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True )
    last_name = models.CharField(max_length=255, null=True, blank=True , )
    #group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='medics')
    specialty = models.CharField(max_length=200)
    patients = models.ManyToManyField(Patient, related_name='patient')
    years_experience = models.PositiveIntegerField()
    


