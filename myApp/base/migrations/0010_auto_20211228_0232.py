# Generated by Django 3.2.9 on 2021-12-28 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20211228_0220'),
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
