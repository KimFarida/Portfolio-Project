from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

"""class CustomGroup(Group):
    users = models.ManyToManyField(User, related_name='custom_groups')
"""


    
class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='Doctor')
    last_name = models.CharField(max_length=255, default='Doctor')
    #group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='medics')
    specialty = models.CharField(max_length=200, null=True, blank=True)
    years_experience = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.specialty} "
    
    
    
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True )
    phone_number = PhoneNumberField()
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
        ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)  
    diagnosis = models.CharField(max_length=200,null=True, blank=True,)
    doctors = models.ManyToManyField(Doctor)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



