# Generated by Django 3.1.5 on 2021-02-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]