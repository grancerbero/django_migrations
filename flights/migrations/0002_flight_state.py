# Generated by Django 5.0 on 2023-12-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
