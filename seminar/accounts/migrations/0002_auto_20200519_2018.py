# Generated by Django 3.0.5 on 2020-05-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='snsaddress',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
