from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
    username = models.CharField(max_length=40, null=True)
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
    image = models.CharField(max_length=256, default="/static/images/background.png")
    amount = models.BigIntegerField()
    akhir_waktu = models.DateField()

    def __str__(self):
        return self.title

class Money(models.Model):
    PAYMENT_MODEL_CHOICES = [
        ("Select...", "Select..."),
        ("Mandiri", "Mandiri"),
        ("BNI", "BNI"),
        ("BRI", "BRI"),
        ("BCA", "BCA"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    pnumber = models.IntegerField()
    donation = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)
    pmethod = models.CharField(max_length=30,
                               choices = PAYMENT_MODEL_CHOICES,
                               default = "Select...",
                               )
    date = models.DateField(blank=True, default=datetime.now())
    ccnumber = models.IntegerField()

class Volunteer(models.Model):
    DIVISI_CHOICES = [
        ("Panitia Inti", "Panitia Inti"),
        ("Kesehatan", "Kesehatan"),
        ("Hubungan Masyarakat", "Hubungan Masyarakat"),
        ("Tenaga Kerja", "Tenaga Kerja"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    divisi = models.CharField(  max_length=255,
                                choices = DIVISI_CHOICES,
                                default = "Panitia Inti",
                            )

    def __str__(self):
        return self.user.username + self.project.title + self.divisi

class Groceries(models.Model):
    SEMBAKO_CHOICES = [
        ("Select...", "Select..."),
        ("Beras", "Beras"),
        ("Garam", "Garam"),
        ("Sirup", "Sirup"),
        ("Gula", "Gula"),
        ("Kopi", "Kopi"),
        ("Minyak", "Minyak"),
        ("Teh", "Teh"),
        ("Lainnya", "Lainnya"),
    ]

    PAYMENT_MODEL_CHOICES = [
        ("Select...", "Select..."),
        ("Mandiri", "Mandiri"),
        ("BNI", "BNI"),
        ("BRI", "BRI"),
        ("BCA", "BCA"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40, null=True)
    date = models.DateField(auto_now_add=True)
    donasi = models.IntegerField()
    sembako = models.CharField(max_length=30,
                            choices = SEMBAKO_CHOICES,
                            default = "Select...",
                            )
    amount = models.BigIntegerField()
    pmethod = models.CharField(max_length=30,
                               choices = PAYMENT_MODEL_CHOICES,
                               default = "Select...",
                               )
    ccnumber = models.IntegerField()

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