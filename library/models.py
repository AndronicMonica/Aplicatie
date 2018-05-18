from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelChoiceField
from django.core import serializers


# Create your models here.

class Book(models.Model):
    titlu = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editura = models.CharField(max_length=100)
    #an_publicare = models.IntegerField(default=2018, validators=[MaxValueValidator(1962), MinValueValidator(2018)])
    variante_disponibilitate = (
        ('DISPONIBIL', 'Disponibil'),
        ('REZERVAT', 'Rezervat'),
        ('INCHIRIAT', 'Inchiriat')
    )
    disponibilitate = models.CharField(max_length=50, choices=variante_disponibilitate, default='DISPONIBIL')

    class Meta:
        default_permissions = ('add', 'view')

    def __str__(self):
        return self.titlu


class Imprumuturi(models.Model):
    nume_prenume = models.CharField(max_length=255)
    data_inceput = models.DateField(null=True, blank=True)
    data_sfarsit = models.DateField(null=True, blank=True)
    titlul_cartii = models.CharField(max_length=255, default='nimic')
    owner = models.ForeignKey("auth.User", models.CASCADE, null=True, blank=True)

    class Meta:
        default_permissions = ('add', 'view')
        permissions = (
            ('read_imprumuturi', 'Can view imprumuturi'),
        )

    def __str__(self):
        return self.nume_prenume
