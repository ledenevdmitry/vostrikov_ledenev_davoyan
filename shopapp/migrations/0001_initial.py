# Generated by Django 2.0 on 2018-01-15 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.CharField(max_length=30)),
                ('weight', models.IntegerField(max_length=5)),
                ('published_date', models.DateTimeField(default=datetime.datetime(2018, 1, 15, 8, 56, 41, 672599, tzinfo=utc))),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
