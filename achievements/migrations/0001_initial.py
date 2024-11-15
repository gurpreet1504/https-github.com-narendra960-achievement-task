# Generated by Django 5.1.3 on 2024-11-06 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_description', models.CharField(max_length=255)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='achievements.achievement')),
            ],
        ),
    ]
