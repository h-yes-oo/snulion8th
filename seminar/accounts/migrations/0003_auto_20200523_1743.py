# Generated by Django 3.0.5 on 2020-05-23 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed', through='accounts.Follow', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follow_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_from', to='accounts.Profile'),
        ),
    ]