from cgitb import text
from pyexpat import model
from tkinter import commondialog
from trace import Trace
from django.db import models

# Create your models here.
class curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.creditos)