# Generated by Django 3.0.5 on 2020-05-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follows',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
