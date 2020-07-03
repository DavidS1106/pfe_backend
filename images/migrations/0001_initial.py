# Generated by Django 3.0 on 2019-12-12 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('categorie_id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categorie', to='images.Categorie')),
            ],
        ),
    ]