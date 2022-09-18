from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(max_length=24, primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=16)
    mobile = models.IntegerField(unique=True)
    status = models.CharField(max_length=8)

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.name + ' ' + self.last_name