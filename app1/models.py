from django.db import models

# Create your models here.
class Register_Data(models.Model):
    name = models.CharField(default="",max_length=100)
    lname = models.CharField(default="",max_length=100)
    email = models.EmailField(default="",max_length=100)
    passw = models.CharField(default="",max_length=100)

    def __str__(self):
        return self.name