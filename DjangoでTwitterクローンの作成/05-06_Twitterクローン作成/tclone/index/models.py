from django.db import models

# Create your models here.
from django.db import models


class NewTweet(models.Model):
    tweet = models.CharField(max_length=255)
