# Generated by Django 2.2.5 on 2019-12-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191212_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='related_to',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
