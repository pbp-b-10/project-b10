# Generated by Django 4.1 on 2022-11-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedulee', '0002_project_volunteer_money_cloth'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.CharField(default='/static/images/background.png', max_length=256),
        ),
    ]
