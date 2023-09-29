# Generated by Django 3.2.9 on 2022-01-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20220101_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
