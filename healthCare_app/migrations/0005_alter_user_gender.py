# Generated by Django 3.2.5 on 2022-11-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthCare_app', '0004_auto_20221120_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=100),
        ),
    ]
