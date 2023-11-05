# Generated by Django 4.0 on 2023-08-02 23:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_alter_usuarios_fecha_nacimiento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.ImageField(blank=True, default='libros/libro_default.png', null=True, upload_to='libros')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='libros.categorias')),
                ('colaborador', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuarios')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
