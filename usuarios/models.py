from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UsuarioPers(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(null=True,blank=True, max_length=1)

class Post(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text


class Manga(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text

class DescripLib(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
    presio = models.TextField(default="")
   
    def __str__(self):
        return self.text

class Autores(models.Model):
    Nombre = models.TextField(default="")
    Descripcion = models.TextField(default="")
    img = models.TextField(default="")
    Nacionalidad = models.TextField(default="")
    F_Muerte = models.TextField(default="")


    def __str__(self):
        return self.Nombre

   