# Generated by Django 3.2.9 on 2021-12-27 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211227_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasaprincipala',
            name='counterParticipanti',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]