# Generated by Django 3.0.8 on 2020-10-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_ad_available_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='person',
            name='public_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='پست الکترونیک'),
        ),
    ]
