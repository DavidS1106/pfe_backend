# Generated by Django 3.0 on 2019-12-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enfants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosupplementaire',
            name='date_naissance',
            field=models.DateTimeField(),
        ),
    ]
