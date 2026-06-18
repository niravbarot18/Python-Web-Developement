from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

USER_TYPENAME=[
    ("user","User"),
    ("buyer","Buyer"),
    ("seller","Seller"),
    ("rent","Rent")
]

USER_GENDER=[
    ("male","MALE"),
    ("female","FEMALE")
]

STATUS=[
    ("active","ACTIVE"),
    ("inactive","INACTIVE")
]


AVAILABLE_QUANTITY=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20')
]

class Role(models.Model):
    user_typename = models.CharField(choices=USER_TYPENAME,max_length=10,verbose_name="Select User Type")

    def __str__(self):
        return self.user_typename

class User(models.Model):
    u_name=models.CharField(max_length=30,verbose_name="User Name")
    u_dp=models.ImageField(upload_to="photos",verbose_name="User Image")
    u_gender=models.CharField(choices=USER_GENDER,verbose_name="User Gender")
    u_email=models.EmailField(max_length=30,verbose_name="User Email")
    u_phone=models.CharField(max_length=10,verbose_name="User Phone")
    u_type=models.ForeignKey(Role,on_delete=models.CASCADE,verbose_name="User Type")
    u_status=models.CharField(choices=STATUS,verbose_name="User Status")
    def __str__(self):
        return self.u_name

    def user_image(self):
        if self.u_dp:
           return mark_safe(f"<img src='{self.u_dp.url}' width='100' />")
        return "No image"

class FurnitureCategory(models.Model):
    cat_name=models.CharField(max_length=30,verbose_name="Furniture Category")
    cat_picture=models.ImageField(upload_to="photos",verbose_name="Furniture Image")
    cat_desc=models.TextField(verbose_name="Furniture Description")
    category_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cat_name

    def furniture_image(self):
        if self.cat_picture:
            return mark_safe(f"<img src='{self.cat_picture.url}' width='100' />")
        return "No image"

class Country(models.Model):
    country_name=models.CharField(max_length=30,verbose_name="Country Name")
    def __str__(self):
        return self.country_name

class State(models.Model):
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name="Country ID",related_name="states")
    state_name=models.CharField(max_length=30,verbose_name="State Name")
    def __str__(self):
        return self.state_name

class City(models.Model):
    state_id=models.ForeignKey(State,on_delete=models.CASCADE,verbose_name="State ID")
    city_name=models.CharField(max_length=30,verbose_name="City Name")
    def __str__(self):
        return self.city_name

class UserAddress(models.Model):
    user_address=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User Address")
    building_name=models.CharField(max_length=30,verbose_name="Building Name")
    street_name=models.CharField(max_length=30,verbose_name="Street Name")
    city_name=models.CharField(max_length=30,verbose_name="City Name")
    pin_code=models.CharField(max_length=30,verbose_name="Pin Code")

class FeedBackDetails(models.Model):
    f_title=models.CharField(max_length=30,verbose_name="Feedback Title")
    f_description=models.TextField(verbose_name="Feedback Description")
    f_by=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Feedback By")
    f_on=models.DateTimeField(auto_now_add=True,verbose_name="Feedback On")
    def __str__(self):
        return self.f_title

class ComplaintDetails(models.Model):
    c_name=models.CharField(max_length=30,verbose_name="Complaint Name")
    c_detail=models.TextField(verbose_name="Complaint Description")
    c_photo=models.ImageField(upload_to="photos",verbose_name="Upload Image")
    c_by=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Complaint By")
    c_on=models.DateTimeField(auto_now_add=True,verbose_name="Complaint On")
    def __str__(self):
        return self.c_name

    def complaint_photo(self):
        if self.c_photo:
            return mark_safe(f"<img src='{self.c_photo.url}' width='100' />")
        return "No image"


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_description = models.TextField()
    brand_logo = models.ImageField(upload_to='photos')

    def brand_image(self):
        if self.brand_logo:
            return mark_safe(f"<img src='{self.brand_logo.url}' width='100' />")
        return "No Image"

    def __str__(self):
        return self.brand_name

class NewFurniture(models.Model):
    f_name = models.CharField(max_length=200,verbose_name="Furniture Name")
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    furniture_description = models.TextField()
    furniture_price = models.DecimalField(max_digits=10,decimal_places=2)
    furniture_image = models.ImageField(upload_to='photos')
    furniture_type = models.ForeignKey(FurnitureCategory,on_delete=models.CASCADE)
    available_quantity = models.IntegerField(choices=AVAILABLE_QUANTITY)

    def furniture_photo(self):
        if self.furniture_image:
            return mark_safe(
                f"<img src='{self.furniture_image.url}' width='100' />"
            )
        return "No Image"

    def __str__(self):
        return self.f_name

class OldFurniture(models.Model):
    old_furniture_name = models.CharField(max_length=200)
    old_furniture_brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    old_furniture_description = models.TextField()
    old_furniture_price = models.DecimalField(max_digits=10,decimal_places=2)
    old_furniture_image = models.ImageField(upload_to='photos')
    old_furniture_type = models.ForeignKey(FurnitureCategory,on_delete=models.CASCADE)
    available_quantity = models.IntegerField(choices=AVAILABLE_QUANTITY)

    def old_furniture_photo(self):
        if self.old_furniture_image:
            return mark_safe(
                f"<img src='{self.old_furniture_image.url}' width='100' />"
            )
        return "No Image"

    def __str__(self):
        return self.old_furniture_name

class RentFurniture(models.Model):
    rent_furniture_name = models.CharField(max_length=200)
    rent_brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    rent_furniture_description = models.TextField()
    rent_furniture_price = models.DecimalField(max_digits=10,decimal_places=2)
    rent_furniture_image = models.ImageField(upload_to='photos',)
    rent_furniture_type = models.ForeignKey(FurnitureCategory,on_delete=models.CASCADE)
    available_quantity = models.IntegerField(choices=AVAILABLE_QUANTITY)

    def rent_furniture_photo(self):
        if self.rent_furniture_image:
            return mark_safe(
                f"<img src='{self.rent_furniture_image.url}' width='100' />"
            )
        return "No Image"

    def __str__(self):
        return self.rent_furniture_name

class NewFurnitureBuying(models.Model):
    furniture = models.ForeignKey(NewFurniture,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.furniture}"

class OldFurnitureBuying(models.Model):
    old_furniture = models.ForeignKey(OldFurniture,on_delete=models.CASCADE)
    user_booking = models.ForeignKey(User,on_delete=models.CASCADE)
    old_booking_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_booking} - {self.old_furniture}"

class RentFurnitureOrder(models.Model):
    rent_furniture = models.ForeignKey(RentFurniture,on_delete=models.CASCADE)
    rent_userid = models.ForeignKey(User,on_delete=models.CASCADE)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    rent_book_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rent_userid} - {self.rent_furniture}"