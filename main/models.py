from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    position = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="team", blank=True, null=True)
