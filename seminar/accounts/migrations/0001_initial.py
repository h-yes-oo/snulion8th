# Generated by Django 3.0.6 on 2020-05-23 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, max_length=20)),
                ('major', models.CharField(blank=True, max_length=20)),
                ('mbti', models.CharField(blank=True, max_length=4)),
                ('follows', models.ManyToManyField(blank=True, related_name='followed', through='accounts.Follow', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='follow_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='follow_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from', to='accounts.Profile'),
        ),
    ]
