from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import MedicalReportForm
from dashboard.models import Patient
from medical_reports.models import MedicalReport
from django.contrib import messages


# Create your views here.


def medical_reports_form(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = request.user
            medical_record.save()
            return redirect('success')
    else:
        form = MedicalReportForm()
    return render(request, 'medical_reports_form.html', {'form': form})

def view_medical_reports(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    medical_reports = MedicalReport.objects.filter(patient=patient)
    return render(request, 'view_medical_reports.html', {'patient': patient, 'medical_reports': medical_reports})