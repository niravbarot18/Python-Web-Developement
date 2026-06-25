from django.db import models
from django.db.models import ForeignKey
from django.utils.safestring import mark_safe

# Create your models here.

ROLE_CHOICES = [
    ("USER", "User"),
    ("BUYER", "Buyer"),
    ("RENT", "Rent"),
]

GENDER_CHOICES = [
    ("MALE", "Male"),
    ("FEMALE", "Female"),
]

STATUS_CHOICES = [
    (1, "Active"),
    (0, "Inactive"),
]

class Role(models.Model):
    user_typename = models.CharField(choices=ROLE_CHOICES,verbose_name="User Type")

    def __str__(self):
        return self.user_typename

class UserDetails(models.Model):
    u_name = models.CharField(verbose_name="User Name", max_length=20)
    u_dp=models.ImageField(upload_to="photos", verbose_name="User Image")
    u_gender=models.CharField(choices=GENDER_CHOICES,verbose_name="Gender")
    u_email=models.EmailField(verbose_name="User Email")
    u_phone=models.CharField(verbose_name="User Phone",max_length=10)
    u_type=models.ForeignKey(Role,verbose_name="User Type",on_delete=models.CASCADE)
    u_status=models.IntegerField(choices=STATUS_CHOICES,verbose_name="User Status")

    def user_image(self):
        if self.u_dp:
            return mark_safe(
                f"<img src='{self.u_dp.url}' width='80' height='80' />"
            )
        return "No Image"

    def __str__(self):
        return self.u_name

class CarCategory(models.Model):
    cat_name = models.CharField(verbose_name="Category Name", max_length=20)
    cat_picture=models.ImageField(upload_to="photos", verbose_name="Category Image")
    cat_description=models.TextField(verbose_name="Category Description")
    category_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

class Country(models.Model):
    country_name = models.CharField(verbose_name="County Name", max_length=20)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country_id=models.ForeignKey(Country,verbose_name="County",on_delete=models.CASCADE)
    state_name = models.CharField(verbose_name="State Name", max_length=20)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state_id = models.ForeignKey(State,verbose_name="State",on_delete=models.CASCADE)
    city_name = models.CharField(verbose_name="City Name", max_length=20)

    def __str__(self):
        return self.city_name

class UserAddress(models.Model):
    u_id = models.ForeignKey(UserDetails,verbose_name="User",on_delete=models.CASCADE)
    building_name = models.CharField(verbose_name="Building Name",max_length=50)
    street_name=models.CharField(verbose_name="Street Name",max_length=100)
    city_name=models.ForeignKey(City,verbose_name="City",on_delete=models.CASCADE)
    pin_code=models.CharField(verbose_name="Pin Code",max_length=20)

def __str__(self):
    return self.u_id.u_name

class FeedbackDetails(models.Model):
    f_title=models.CharField(verbose_name="Feedback Title",max_length=20)
    f_description=models.TextField(verbose_name="Feedback Description")
    f_by=models.ForeignKey(UserDetails,verbose_name="Feedback By",on_delete=models.CASCADE)
    f_on=models.DateTimeField(verbose_name="Feedback On",auto_now_add=True)

    def __str__(self):
        return self.f_title

class ComplaintDetails(models.Model):
    c_name=models.CharField(verbose_name="Complaint Name",max_length=20)
    c_detail=models.TextField(verbose_name="Complaint Description")
    c_photo=models.ImageField(upload_to="photos", verbose_name="Complaint Image")
    c_by=models.ForeignKey(UserDetails,verbose_name="Complaint By",on_delete=models.CASCADE)
    c_on=models.DateTimeField(verbose_name="Complaint On",auto_now_add=True)

    def complaint_photo(self):
        if self.c_photo:
            return mark_safe(
                f"<img src='{self.c_photo.url}' width='80' height='80' />"
            )
        return "No Image"

    def __str__(self):
        return self.c_name
