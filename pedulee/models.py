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

class Pakaian(models.Model):
    JENIS_CHOICES = [
        ("kemeja", "Kemeja"),
        ("kaos", "Kaos"),
        ("celana", "Celana"),
        ("rok", "Rok"),
        ("sepatu", "Sepatu"),
        ("aksesoris", "Aksesoris"),
        ("lainnya", "Lainnya"),
    ]
    BAHAN_CHOICES = [
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
    TIPE_CHOICES = [
        ("perempuan", "Perempuan"),
        ("laki", "Laki-kaki"),
        ("anakPerempuan", "Anak perempuan"),
        ("anakLaki", "Anak laki-laki"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    jenis = models.CharField(max_length=30,
                            choices = JENIS_CHOICES,
                            default = "kemeja",
                            )
    tipe_pakaian = models.CharField(max_length=30,
                            choices = TIPE_CHOICES,
                            default = "perempuan",
                            )
    bahan = models.CharField(max_length=30,
                            choices = BAHAN_CHOICES,
                            default = "katun",
                            )