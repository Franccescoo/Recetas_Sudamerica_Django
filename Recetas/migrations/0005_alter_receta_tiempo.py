# Generated by Django 4.0.4 on 2022-05-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0004_receta_dificultad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='tiempo',
            field=models.IntegerField(),
        ),
    ]
