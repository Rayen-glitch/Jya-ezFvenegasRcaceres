# Generated by Django 2.2.6 on 2019-11-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('nick', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contra', models.CharField(max_length=30)),
            ],
        ),
    ]