# Generated by Django 5.0.4 on 2024-04-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='sale',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
