# Generated by Django 3.2.9 on 2022-01-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20220101_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasaprincipala',
            name='counterParticipanti',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clasaprincipala',
            name='listaParticipanti',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
