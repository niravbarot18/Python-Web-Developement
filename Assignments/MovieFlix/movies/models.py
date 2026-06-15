from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

STATUS_CHOICES = [
    (0, "Inactive"),
    (1, "Active"),
]

class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name


class Actor(models.Model):
    a_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="Actor's State")
    a_country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Actor's Country")
    a_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Actor's City")

    a_name = models.CharField(max_length=100, verbose_name="Actor's Name")

    a_profile = models.ImageField(upload_to="photos", verbose_name="Actor's Image")

    a_bio = models.TextField(verbose_name="Actor's Bio")

    a_nationality = models.CharField(max_length=100, verbose_name="Actor's Nationality")

    a_awards = models.CharField(max_length=255, verbose_name="Actor's Awards")

    a_gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Actor's Gender",
    )

    a_birthdate = models.DateField(verbose_name="Actor's Birthdate")

    def __str__(self):
        return self.a_name

    def actor_image(self):
        return mark_safe("<img src='{}' width='100' />".format(self.a_profile.url))

class User(models.Model):
    u_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="User's State")
    u_country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="User's Country")
    u_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="User's City")

    u_name = models.CharField(max_length=100, verbose_name="User's Name")

    u_profile = models.ImageField(upload_to="photos", verbose_name="User's Image")

    u_gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="User's Gender",
    )

    u_email = models.EmailField(unique=True, verbose_name="User's Email")

    u_phone = models.CharField(max_length=15, verbose_name="User's Phone")

    u_status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name="User's Status",
    )

    u_date_joined = models.DateField(auto_now_add=True, verbose_name="User's Date Joined")

    def __str__(self):
        return self.u_name

    def user_image(self):
        return mark_safe("<img src='{}' width='100' />".format(self.u_profile.url))

class Director(models.Model):
    d_state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name="Director's State")
    d_country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Director's Country")
    d_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Director's City")

    d_name = models.CharField(max_length=100, verbose_name="Director's Name")
    d_image = models.ImageField(upload_to="photos", verbose_name="Director's Image")
    d_bio = models.TextField(verbose_name="Director's Bio")

    d_nationality = models.CharField(max_length=100, verbose_name="Director's Nationality")
    d_awards = models.CharField(max_length=255, verbose_name="Director's Awards")

    d_gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        verbose_name="Director's Gender",
    )

    def __str__(self):
        return self.d_name

    def director_image(self):
        return mark_safe("<img src='{}' width='100' />".format(self.d_image.url))

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    release_year = models.IntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    actors = models.ManyToManyField(
        Actor
    )

    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE
    )

    trailer = models.URLField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_actors(self):
        return ",".join([actor.a_name for actor in self.actors.all()])

    get_actors.short_description = "Actors"

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.movie}"

class Watchlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )

    added_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user} - {self.movie}"