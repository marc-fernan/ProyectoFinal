# Generated by Django 4.2.4 on 2023-09-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLab', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tramite',
            old_name='fechaTramite',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='tramite',
            old_name='nombre',
            new_name='motivo',
        ),
        migrations.AlterField(
            model_name='tramite',
            name='estado',
            field=models.CharField(max_length=50),
        ),
    ]
