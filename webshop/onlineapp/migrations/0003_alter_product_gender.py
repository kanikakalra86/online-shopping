# Generated by Django 3.2.13 on 2022-06-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Female'), (1, 'Male')], null=True),
        ),
    ]
