# Generated by Django 5.0.7 on 2024-07-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroPersonas', '0011_delete_personaborrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
