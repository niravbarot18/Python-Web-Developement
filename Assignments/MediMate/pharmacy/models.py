from django.db import models
from django.db.models import ForeignKey
from django.utils.safestring import mark_safe

# Create your models here.
USERTYPE_NAME=[
    ('user','User'),
    ('buyer','Buyer'),
    ('seller','Seller'),
    ('rent','Rent')
]

USER_STATUS=[
    ('0','Active'),
    ('1','Inactive'),
]

USER_GENDER=[
    ('male','Male'),
    ('female','Female'),
]

class Role(models.Model):
    user_type = models.CharField(choices=USERTYPE_NAME)
    def __str__(self):
        return self.user_type

class UserDetail(models.Model):
    u_name= models.CharField(max_length=11,verbose_name='User Name')
    u_dp = models.ImageField(upload_to="photos",verbose_name="User Image")
    u_gender = models.CharField(choices=USER_GENDER,verbose_name='User Gender')
    u_email = models.EmailField(verbose_name='User Email')
    u_phone=models.CharField(max_length=10,verbose_name='User Phone')
    u_type = models.CharField(choices=USERTYPE_NAME,verbose_name='User Type')
    u_status=models.CharField(choices=USER_STATUS,verbose_name='User Status')

    def __str__(self):
        return self.u_name

    def user_image(self):
        if self.u_dp:
           return mark_safe(f"<img src='{self.u_dp.url}' width='100' />")
        return "No image"

class GadgetCategory(models.Model):
    cat_name = models.CharField(max_length=20,verbose_name='Gadget Category')
    cat_picture = models.ImageField(upload_to="photos",verbose_name='Category Image')
    cat_description = models.TextField(verbose_name='Category Description')
    category_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    def cat_image(self):
        if self.cat_picture:
            return mark_safe(f"<img src='{self.cat_image.url}' width='100' />")
        return "No image"

class Country(models.Model):
    country_name=models.CharField(max_length=20,verbose_name='Country Name')
    def __str__(self):
        return self.country_name

class State(models.Model):
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name='Country ID')
    state_name=models.CharField(max_length=20,verbose_name='State Name')
    def __str__(self):
        return self.state_name

class City(models.Model):
    state_id=ForeignKey(State,on_delete=models.CASCADE,verbose_name='State ID')
    city_name=models.CharField(max_length=20,verbose_name='City Name')
    def __str__(self):
        return self.city_name
    
class UserAddress(models.Model):
    u_id=models.ForeignKey(UserDetail,on_delete=models.CASCADE,verbose_name='User ID')
    building_name=models.CharField(max_length=20,verbose_name='Building Name')
    street_name=models.CharField(max_length=20,verbose_name='Street Name')
    city_name=models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='City Name')
    pincode=models.CharField(max_length=20,verbose_name='PINCODE')

    def __str__(self):
        return self.u_id

class FeedbackDetail(models.Model):
    f_title=models.CharField(max_length=20,verbose_name='Feedback Title')
    f_description=models.TextField(verbose_name='Feedback Description')
    f_by=models.ForeignKey(UserDetail,on_delete=models.CASCADE,verbose_name='Feedback By')
    f_on=models.DateTimeField(auto_now_add=True,verbose_name='Feedback On')
    def __str__(self):
        return self.f_title

class Complaint(models.Model):
    c_name=models.CharField(max_length=20,verbose_name='Complaint Name')
    c_details=models.TextField(verbose_name='Complaint Details')
    c_photo=models.ImageField(upload_to="photos",verbose_name='Complaint Photo')
    c_by=models.ForeignKey(UserDetail,on_delete=models.CASCADE,verbose_name='Complaint By')
    c_on=models.DateTimeField(auto_now_add=True,verbose_name='Complaint On')

    def __str__(self):
        return self.c_name

    def c_image(self):
        if self.c_photo:
            return mark_safe(f"<img src='{self.c_photo.url}' width='100' />")
        return "No image"