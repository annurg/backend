# Generated by Django 2.2.2 on 2020-09-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='temperature',
            field=models.FloatField(default=40, max_length=3),
        ),
        migrations.AddField(
            model_name='year',
            name='temperature',
            field=models.FloatField(default=40, max_length=3),
        ),
    ]
