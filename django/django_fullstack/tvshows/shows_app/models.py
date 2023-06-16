from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    description = models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

