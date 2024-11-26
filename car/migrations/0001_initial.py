# Generated by Django 5.1.3 on 2024-11-26 13:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('car_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('production_year', models.SmallIntegerField()),
                ('description', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]