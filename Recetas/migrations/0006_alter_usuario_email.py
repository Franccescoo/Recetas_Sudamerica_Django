# Generated by Django 4.0.4 on 2022-05-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0005_alter_receta_tiempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
