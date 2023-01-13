from django.urls import path
from . import views

urlpatterns = [
    path('medical-reports-form', views.medical_reports_form, name='medical_reports_html'),
    path('view-medical-reports/<str:patient_id>/', views.view_medical_reports, name='view_medical_reports_html'),
    path('edit-medical-reports/<int:report_id>/', views.edit_medical_reports, name='edit_medical_report'),
    path('delete-medical-reports/<int:report_id>/', views.delete_medical_reports, name='delete_medical_report'),
   
]