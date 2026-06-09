from django.contrib import admin
from .models import Patients

# Register your models here.

@admin.register(Patients)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','phone','address','blood_group','doctor_name','is_admitted','timestamp')