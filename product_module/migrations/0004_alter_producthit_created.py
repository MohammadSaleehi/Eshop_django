# Generated by Django 4.2.3 on 2023-09-19 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_producthit_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthit',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 20, 0, 9, 34, 136250), verbose_name='زمان مشاهده'),
        ),
    ]