from random import choices
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    birthdate = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Cloth(models.Model):
    CLOTH_MODEL_CHOICES = [
        ("kemeja", "Kemeja"),
        ("kaos", "Kaos"),
        ("celana", "Celana"),
        ("rok", "Rok"),
        ("sepatu", "Sepatu"),
        ("aksesoris", "Aksesoris"),
        ("lainnya", "Lainnya"),
    ]
    MATERIAL_CHOICES = [
        ("katun", "Katun"),
        ("linen", "Linen"),
        ("denim", "Denim"),
        ("kulit", "Kulit"),
        ("polyester", "Polyester"),
        ("suede", "Suede"),
        ("sutra", "Sutra"),
        ("velvet", "Velvet"),
        ("rajut", "Rajut"),
        ("rayon", "Rayon"),
        ("jersey", "Jersey"),
        ("twistcone", "Twistcone"),
        ("lainnya", "Lainnya"),
    ]
    TYPE_CHOICES = [
        ("perempuan", "Perempuan"),
        ("laki", "Laki-laki"),
        ("anakPerempuan", "Anak perempuan"),
        ("anakLaki", "Anak laki-laki"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    cloth_model = models.CharField(max_length=30,
                            choices = CLOTH_MODEL_CHOICES,
                            default = "kemeja",
                            )
    material = models.CharField(max_length=30,
                            choices = MATERIAL_CHOICES,
                            default = "katun",
                            )
    type = models.CharField(max_length=30,
                            choices = TYPE_CHOICES,
                            default = "perempuan",
                            )
    