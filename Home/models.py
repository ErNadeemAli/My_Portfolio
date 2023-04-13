from django.db import models

# Create your models here.

class OurUser(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=200)
    number=models.CharField(max_length=15)
    option=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.first_name
    