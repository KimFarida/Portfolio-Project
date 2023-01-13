from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from dashboard.models import Doctor, Patient
from appointments.models import Appointment

# Create your models here.

BLOOD_TYPE =(

    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
)

class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    #doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    address= models.TextField()
    age= models.PositiveIntegerField()
    weight= models.PositiveIntegerField()
    bloodgroup= models.CharField(max_length=25,choices=BLOOD_TYPE,default= "O+",)
    medical_history = models.TextField(null=True, blank=True)
    date = models.DateField()
    symptoms= models.TextField(null=True, blank=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes=models.TextField(null=True, blank=True) 
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.patient.first_name+' '+self.patient.last_name