# Generated by Django 4.2.14 on 2024-08-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_habitacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45)], unique=True)),
                ('nombre_habitacion', models.CharField(choices=[('suite', 'Suite'), ('duplex', 'Duplex'), ('simple', 'Simple')], max_length=20)),
                ('estado', models.CharField(choices=[('libre', 'Libre'), ('ocupada', 'Ocupada'), ('reservada', 'Reservada')], max_length=10)),
                ('capacidad', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('notas_habitaciones', models.TextField(blank=True, max_length=1000)),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
            ],
        ),
    ]
