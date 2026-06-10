from django.db import models

# Create your models here.

class PlayerCategory(models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class PlayerTeam(models.Model):
    team_name = models.CharField(max_length=35)
    team_description = models.TextField()

    def __str__(self):
        return self.team_name

class Player(models.Model):
    name = models.CharField(max_length=30)
    category_id = models.ForeignKey(PlayerCategory, on_delete=models.CASCADE)
    team_id = models.ForeignKey(PlayerTeam, on_delete=models.CASCADE)
    runs=models.IntegerField()
    wickets=models.IntegerField()
    hundreds=models.IntegerField()
    fifties=models.IntegerField()
    jersey_no=models.IntegerField()

