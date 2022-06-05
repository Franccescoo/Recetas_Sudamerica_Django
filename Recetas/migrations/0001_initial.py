# Generated by Django 4.0.4 on 2022-06-04 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('idNacionalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nomNacionalidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RolUsuario',
            fields=[
                ('idNacionalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nomNacionalidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomUsuario', models.CharField(max_length=30)),
                ('apellidoCompleto', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank='', default='foto_perfil/foto_perfil_default.png', upload_to='foto_perfil')),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('idReceta', models.AutoField(primary_key=True, serialize=False)),
                ('nomReceta', models.CharField(max_length=30)),
                ('ingrediente', models.CharField(max_length=1000)),
                ('preparacion', models.CharField(max_length=2000)),
                ('tiempo', models.IntegerField()),
                ('fotoReceta', models.ImageField(upload_to='foto_receta')),
                ('Nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recetas.nacionalidad')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recetas.usuario')),
            ],
        ),
    ]
