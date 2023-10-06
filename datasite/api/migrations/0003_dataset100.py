# Generated by Django 4.2.6 on 2023-10-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_dataset234_dataset282_dataset343_dataset355_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset100',
            fields=[
                ('license_plate', models.TextField(primary_key=True, serialize=False)),
                ('seq', models.TextField(blank=True, null=True)),
                ('unnormalized_read_counts', models.BigIntegerField(blank=True, null=True)),
                ('isomirmap_flags', models.TextField(blank=True, null=True)),
                ('mintmap_flags', models.TextField(blank=True, null=True)),
                ('minrmap_flags', models.TextField(blank=True, null=True)),
                ('yrfmap_flags', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dataset_100',
                'managed': False,
            },
        ),
    ]