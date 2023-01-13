from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import MedicalReportForm, MedicalReportEditForm
from dashboard.models import Patient
from medical_reports.models import MedicalReport
from django.contrib import messages


# Create your views here.


def medical_reports_form(request, patient_id):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST)
        if form.is_valid():
            medical_report = form.save(commit=False)
            medical_report.patient = request.user
            medical_report.save()
            return redirect('success')

        patient = Patient.objects.get(id=patient_id)
        medical_reports = MedicalReport.objects.filter(patient=patient)
        if MedicalReport.editable == True:
            if request.user.groups.filter(name='doctors').exists() and request.user.has_perm('view_medical_reports'):
                # render the template with the patient's information
                context = {'patient': patient, 'medical_reports': medical_reports,'editable':editable}
            return render(request, 'view_medical_reports.html', context)
        else:
            editable = False
            # redirect to an error page
            return redirect('permission_denied')

    else:
        form = MedicalReportForm()
    return render(request, 'medical_reports_form.html', {'form': form})

def view_medical_reports(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    medical_reports = MedicalReport.objects.filter(patient=patient)
    return render(request, 'view_medical_reports.html', {'patient': patient, 'medical_reports': medical_reports})

def edit_medical_reports(request, record_id):
    medical_report = MedicalReport.objects.get(id=record_id)
    if request.user.groups.filter(name='doctors').exists() and request.user.has_perm('change_medical_report'):
        if request.method == 'POST':
            form =MedicalReportEditForm(request.POST, instance=medical_report)
            if form.is_valid():
                form.save()
                return redirect('view_medical_reports', patient_id=medical_report.patient.id)
        else:
            form = MedicalReportEditForm(instance=medical_report)
        return render(request, 'edit_medical_reports.html', {'form': form, 'record': medical_report})
        
    else:
        # redirect to an error page
        return redirect('permission_denied')

def delete_medical_reports(request, record_id):
    # retrieve the medical record from the database
    medical_report = MedicalReport.objects.get(id=record_id)
    # check if the user is a doctor and has the permission to delete the record
    if request.user.groups.filter(name='doctors').exists() and request.user.has_perm('delete_medical_report'):
        # delete the medical record
        medical_report.delete()
        messages.success(request, 'Medical record deleted successfully')
        return redirect('view_medical_reports', patient_id=medical_report.patient.id)
    else:
        # redirect to an error page
        return redirect('permission_denied')