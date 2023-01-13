from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from dashboard.models import Doctor
# Create your models here.

# DOCTOR_CHOICES = (
#     ("Dr. Dan Nwosu-Pediatrics","Dr. Dan Nwosu-Pediatrics"),
#     ("Dr. Halima Danjuma-Gyneacology","Dr. Halima Danjuma-Gyneacology"),
#     ("Dr. Victor Adegoke-Dentistry", "Dr. Victor Adegoke-Dentistry"),
#     ("Dr. Jeddah Olaleye-Plastic Surgery","Dr. Jeddah Olaleye-Plastic Surgery" ),
#     ("Dr. Elo Mensah-Cardiology","Dr. Elo Mensah-Cardiology"),
#     ("Dr. Jesse Jackson-General Medicine","Dr. Jesse Jackson-General Medicine"),
#     ("Dr. Claire Brown-Pathology","Dr. Claire Brown-Pathology" ),
#     ("Dr. Shaun Murphy-General Surgery","Dr. Shaun Murphy-General Surgery") ,    

#)
DOCTOR_CHOICES =[]

SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("HomeCare/Special Care", "HomeCare/Special Care"),
    )
TIME_CHOICES = (
    ("7 AM", "7:30 AM"),
    ("8 AM", "8:30 AM"),
    ("9 AM", "9:30 AM"),
    ("10 AM", "10:30 AM"),
    ("11 AM", "11:30 AM"),
    ("1:00 PM", "1:30 PM"),
    ("2 PM", "2:30 PM"),
    ("3 PM", "3:30 PM"),
    ("4 PM", "4:30 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}  | day: {self.day} | time: {self.time} |doctor: {self.doctor} "