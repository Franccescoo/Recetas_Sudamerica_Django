# Generated by Django 4.0.4 on 2022-06-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recetas', '0007_alter_usuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank='', upload_to='foto_perfil'),
        ),
    ]