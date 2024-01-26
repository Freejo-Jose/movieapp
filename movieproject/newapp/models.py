from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    pict=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
