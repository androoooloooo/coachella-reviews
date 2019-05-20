from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    artist = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    date = models.DateField()
    coachellaYear = models.DateField()
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.review_text
