from django.db import models

# Create your models here.

course_names = [
    ('python', 'Python'),
    ('flutter', 'Flutter'),
    ('django', 'Django'),
    ('react', 'React'),
]

dept = [
    ('sales', 'Sales'),
    ('marketing', 'Marketing'),
    ('development', 'Development'),
    ('teaching', 'Teaching'),
]

class Student(models.Model):
    f_name=models.CharField(max_length=100,verbose_name="First Name")
    l_name=models.CharField(max_length=100,verbose_name="Last Name")
    dob=models.DateField(verbose_name="Date of Birth")
    doj=models.DateField(verbose_name="Date of Joining")
    contact=models.CharField(max_length=10)
    email=models.EmailField()

class Course(models.Model):
    course_title=models.CharField(max_length=100,verbose_name="Course Title")
    course_code=models.CharField(max_length=100,verbose_name="Course Code")
    price=models.FloatField(verbose_name="Price")
    desc=models.TextField(verbose_name="Description")
    start_date=models.DateField(verbose_name="Start Date")
    end_date=models.DateField(verbose_name="End Date")
    is_available=models.BooleanField(verbose_name="Is Available")

class Instructor(models.Model):
    f_name=models.CharField(max_length=50,verbose_name="First Name")
    l_name=models.CharField(max_length=50,verbose_name="Last Name")
    dob=models.DateField(verbose_name="Date of Birth")
    doj=models.DateField(verbose_name="Date of Joining")
    dept=models.CharField(max_length=50,verbose_name="Department")
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    is_active=models.BooleanField(verbose_name="Is Active")
    linkedinURL=models.URLField(verbose_name="Linkedin URL")