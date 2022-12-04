# Generated by Django 4.1 on 2022-11-02 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedulee', '0004_alter_volunteer_divisi_groceries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('golongan', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=30)),
                ('rhesus', models.CharField(choices=[('+', '+'), ('-', '-')], max_length=30)),
                ('penyakit_bawaan', models.CharField(max_length=30)),
                ('lokasi_donor', models.CharField(choices=[('Jakarta', 'Jakarta'), ('Depok', 'Depok'), ('Bogor', 'Bogor'), ('bandung', 'Bandung')], max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]