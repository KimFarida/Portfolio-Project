from django.contrib import admin
from .models import Patient, Doctor


# Register your models here.

#admin.site.register(CustomGroup)
admin.site.register(Patient)
admin.site.register(Doctor)
