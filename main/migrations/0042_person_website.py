# Generated by Django 3.0.8 on 2020-08-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20200831_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='website',
            field=models.URLField(blank=True, verbose_name='وبسایت'),
        ),
    ]
