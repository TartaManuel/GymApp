# Generated by Django 3.2.9 on 2021-12-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211227_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasaprincipala',
            name='counterParticipanti',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clasaprincipala',
            name='listaParticipanti',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]