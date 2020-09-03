from django.db import models

# Create your models here.
class CRUDapi(models.Model):
	name = models.CharField(max_length=50, blank=False)
	collage = models.CharField(max_length=70, blank=False)
	gender = models.BooleanField()