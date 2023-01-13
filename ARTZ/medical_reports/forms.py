from django import forms
from .models import MedicalReport
from django.core.exceptions import ValidationError

class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['age','weight', 'bloodgroup', 'medical_history','date', 'symptoms','diagnosis','treatment',  'notes']


class MedicalReportEditForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['age','weight', 'bloodgroup', 'medical_history','date', 'symptoms','diagnosis','treatment',  'notes']