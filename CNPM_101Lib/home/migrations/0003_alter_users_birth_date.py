# Generated by Django 3.2.9 on 2021-12-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211203_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
