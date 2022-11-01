from operator import mod
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
        ("Kemeja", "Kemeja"),
        ("Kaos", "Kaos"),
        ("Celana", "Celana"),
        ("Rok", "Rok"),
        ("Sepatu", "Sepatu"),
        ("Aksesoris", "Aksesoris"),
        ("Lainnya", "Lainnya"),
    ]
    MATERIAL_CHOICES = [
        ("Katun", "Katun"),
        ("Linen", "Linen"),
        ("Denim", "Denim"),
        ("Kulit", "Kulit"),
        ("Polyester", "Polyester"),
        ("Suede", "Suede"),
        ("Sutra", "Sutra"),
        ("Velvet", "Velvet"),
        ("Rajut", "Rajut"),
        ("Rayon", "Rayon"),
        ("Jersey", "Jersey"),
        ("Twistcone", "Twistcone"),
        ("Lainnya", "Lainnya"),
    ]
    TYPE_CHOICES = [
        ("Perempuan", "Perempuan"),
        ("Laki-laki", "Laki-laki"),
        ("Anak perempuan", "Anak perempuan"),
        ("Anak laki-laki", "Anak laki-laki"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    cloth_model = models.CharField(max_length=30,
                            choices = CLOTH_MODEL_CHOICES,
                            default = "Kemeja",
                            )
    material = models.CharField(max_length=30,
                            choices = MATERIAL_CHOICES,
                            default = "Katun",
                            )
    type = models.CharField(max_length=30,
                            choices = TYPE_CHOICES,
                            default = "Perempuan",
                            )
                            
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    link = models.CharField(max_length=256)
    amount = models.BigIntegerField()
    akhir_waktu = models.DateField()

    def __str__(self):
        return self.title

class Blood(models.Model):
    goldar =(
        ("A", "A"),
        ("B", "B"),
        ("O", "O"),
        ("AB", "AB"),
    )
    lokasi = (
        ("Jakarta", "Jakarta"),
        ("Depok", "Depok"),
        ("Bogor", "Bogor"),
        ("bandung", "Bandung"),
        )

    rhesus_darah = (
        ("+", "+"),
        ("-", "-"),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    golongan = models.CharField(choices = goldar,max_length=30)
    rhesus = models.CharField(choices = rhesus_darah,max_length=30)
    penyakit_bawaan = models.CharField(max_length=30)
    lokasi_donor = models.CharField(choices=lokasi,max_length=30)