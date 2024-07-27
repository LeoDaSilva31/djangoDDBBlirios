# Generated by Django 5.0.7 on 2024-07-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroPersonas', '0002_remove_habitacion_personas_habitacion_datos_personas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='ingreso',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]