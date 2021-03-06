# Generated by Django 2.2.5 on 2020-10-24 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0002_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='propiedad.Propietario'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='gasto_comun',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
