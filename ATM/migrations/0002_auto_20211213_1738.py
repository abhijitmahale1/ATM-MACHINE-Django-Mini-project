# Generated by Django 3.2.9 on 2021-12-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='num',
            field=models.IntegerField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='anum',
            field=models.IntegerField(max_length=20),
        ),
    ]