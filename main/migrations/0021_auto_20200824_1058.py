# Generated by Django 3.0.8 on 2020-08-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200824_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/', verbose_name='آواتار'),
        ),
    ]
