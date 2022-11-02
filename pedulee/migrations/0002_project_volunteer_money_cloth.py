# Generated by Django 4.1 on 2022-11-02 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedulee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('link', models.CharField(max_length=256)),
                ('amount', models.BigIntegerField()),
                ('akhir_waktu', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divisi', models.CharField(choices=[('Logistics', 'Logistics'), ('Secretary', 'Secretary'), ('Worker', 'Worker')], default='Logistics', max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedulee.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('pnumber', models.IntegerField()),
                ('donation', models.CharField(max_length=1024)),
                ('message', models.CharField(max_length=1024)),
                ('pmethod', models.CharField(choices=[('Select...', 'Select...'), ('Mandiri', 'Mandiri'), ('BNI', 'BNI'), ('BRI', 'BRI'), ('BCA', 'BCA')], default='Select...', max_length=30)),
                ('ccnumber', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('cloth_model', models.CharField(choices=[('Kemeja', 'Kemeja'), ('Kaos', 'Kaos'), ('Celana', 'Celana'), ('Rok', 'Rok'), ('Sepatu', 'Sepatu'), ('Aksesoris', 'Aksesoris'), ('Lainnya', 'Lainnya')], default='Kemeja', max_length=30)),
                ('material', models.CharField(choices=[('Katun', 'Katun'), ('Linen', 'Linen'), ('Denim', 'Denim'), ('Kulit', 'Kulit'), ('Polyester', 'Polyester'), ('Suede', 'Suede'), ('Sutra', 'Sutra'), ('Velvet', 'Velvet'), ('Rajut', 'Rajut'), ('Rayon', 'Rayon'), ('Jersey', 'Jersey'), ('Twistcone', 'Twistcone'), ('Lainnya', 'Lainnya')], default='Katun', max_length=30)),
                ('type', models.CharField(choices=[('Perempuan', 'Perempuan'), ('Laki-laki', 'Laki-laki'), ('Anak perempuan', 'Anak perempuan'), ('Anak laki-laki', 'Anak laki-laki')], default='Perempuan', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]