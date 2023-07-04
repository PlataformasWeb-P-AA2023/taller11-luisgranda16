# Generated by Django 4.2.2 on 2023-07-04 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Residencial', 'Comercial'), ('Comercial', 'Residencial')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=30)),
                ('costo', models.IntegerField(verbose_name='costo del departamento')),
                ('numeroCuartos', models.IntegerField(verbose_name='número de cuartos')),
                ('edificio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Departamentos', to='administrativo.edificio')),
            ],
        ),
    ]