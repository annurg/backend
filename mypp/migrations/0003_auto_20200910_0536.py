# Generated by Django 2.2.2 on 2020-09-10 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypp', '0002_auto_20200910_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='mypp.City'),
        ),
    ]