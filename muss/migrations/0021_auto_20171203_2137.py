# Generated by Django 2.0 on 2017-12-04 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muss', '0020_register_is_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
