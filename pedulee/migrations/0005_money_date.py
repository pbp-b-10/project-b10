# Generated by Django 4.1 on 2022-11-02 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedulee', '0004_alter_volunteer_divisi_groceries'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 2, 23, 12, 19, 215902)),
        ),
    ]