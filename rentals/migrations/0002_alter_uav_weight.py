# Generated by Django 4.2.13 on 2024-05-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uav',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
