from django.urls import path
from . import views

urlpatterns = [
    path('medical-reports-form', views.medical_reports_form, name='medical_reports_html'),
    path('view-medical-reports/<str:patient_id>/', views.view_medical_reports, name='view_medical_reports_html'),
   
]