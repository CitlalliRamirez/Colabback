# Generated by Django 3.2.6 on 2021-08-24 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('profesor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
