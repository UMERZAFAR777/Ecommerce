# Generated by Django 5.0.4 on 2024-04-26 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_category')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
    ]
