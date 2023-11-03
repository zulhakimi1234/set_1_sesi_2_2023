from django.db import models

# Create your models here.

class description(models.Model):
   name = models.TextField()
   text = models.TextField()