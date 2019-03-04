from django.db import models

class NewTweet(models.Model):
    tweet = models.CharField(max_length=255)