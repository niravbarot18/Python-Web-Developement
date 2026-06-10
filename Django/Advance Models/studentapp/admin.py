from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("f_name","l_name","dob","doj","contact","email")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_title","course_code","price","desc","start_date","end_date","is_available")

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("f_name","l_name","dob","doj","contact","email","is_active","linkedinURL")
