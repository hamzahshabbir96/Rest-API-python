# Generated by Django 3.2.6 on 2021-08-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcollection',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
