from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Models):
    Artist = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    date = models.DateField()
    coachellaYear = models.DateField()
