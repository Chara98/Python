from django.db import models

# Create your models here.
class members(models.Model):
    User_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='static', default=None)
    purpose = models.CharField(max_length=30)
