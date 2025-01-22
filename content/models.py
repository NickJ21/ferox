from django.db import models

# Create your models here.
class Project(models.Model):
    client = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return f''' {self.client} '''