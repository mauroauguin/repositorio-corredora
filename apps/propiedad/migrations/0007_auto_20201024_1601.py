# Generated by Django 2.2.5 on 2020-10-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedad', '0006_auto_20201024_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='evaluacion',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Evaluación'),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='trato',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Trato'),
        ),
    ]
