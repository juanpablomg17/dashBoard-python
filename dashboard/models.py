from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Resto de ciertas enfermedades infecciosas y parasitarias', 'Resto de ciertas enfermedades infecciosas y parasitarias'),
    ('Otras causas', 'Otras causas'),
)

class Death(models.Model):
    year = models.CharField(max_length=100, null=True)
    cantidad = models.PositiveIntegerField(null=True)
    categoria = models.CharField(max_length=255, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.year}'
    
    
class Birth(models.Model):
    year = models.CharField(max_length=100, null=True)
    cantidad = models.PositiveIntegerField(null=True)
    categoria = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.year}'
    
class Education(models.Model):
    year = models.CharField(max_length=100, null=True)
    cantidad = models.PositiveIntegerField(null=True)
    categoria = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.year}'



