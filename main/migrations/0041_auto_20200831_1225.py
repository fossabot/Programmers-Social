# Generated by Django 3.0.8 on 2020-08-31 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_project_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='github',
            field=models.URLField(blank=True, verbose_name='گیت\u200cهاب'),
        ),
        migrations.AddField(
            model_name='person',
            name='gitlab',
            field=models.URLField(blank=True, verbose_name='گیت\u200cلب'),
        ),
        migrations.AddField(
            model_name='person',
            name='linkedin',
            field=models.URLField(blank=True, verbose_name='لینکدین'),
        ),
        migrations.AddField(
            model_name='person',
            name='stackowerflow',
            field=models.URLField(blank=True, verbose_name='استک اورفلو'),
        ),
    ]
