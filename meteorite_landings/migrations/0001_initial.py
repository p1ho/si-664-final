# Generated by Django 2.1.4 on 2018-12-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryArea',
            fields=[
                ('country_area_id', models.AutoField(primary_key=True, serialize=False)),
                ('country_area_name', models.CharField(max_length=255, unique=True)),
                ('m49_code', models.SmallIntegerField()),
                ('iso_alpha3_code', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name': 'UNESCO Country/Area',
                'verbose_name_plural': 'UNESCO Countries/Areas',
                'db_table': 'country_area',
                'ordering': ['country_area_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DevStatus',
            fields=[
                ('dev_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('dev_status_name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name': 'Development Status',
                'verbose_name_plural': 'Development Statuses',
                'db_table': 'dev_status',
                'ordering': ['dev_status_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IntermediateRegion',
            fields=[
                ('intermediate_region_id', models.AutoField(primary_key=True, serialize=False)),
                ('intermediate_region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNESCO Intermediate Region',
                'verbose_name_plural': 'UNESCO Intermediate Regions',
                'db_table': 'intermediate_region',
                'ordering': ['intermediate_region_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'UNESCO Country Location',
                'verbose_name_plural': 'UNESCO Country Locations',
                'db_table': 'location',
                'ordering': ['location_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeteoriteClass',
            fields=[
                ('meteorite_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('definition', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Meteorite Class',
                'verbose_name_plural': 'Meteorite Classes',
                'db_table': 'meteorite_class',
                'ordering': ['code'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MeteoriteLanding',
            fields=[
                ('meteorite_landing_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('average_mass', models.FloatField()),
                ('max_mass', models.FloatField()),
                ('min_mass', models.FloatField()),
            ],
            options={
                'verbose_name': 'Meteorite Landing',
                'verbose_name_plural': 'Meteorite Landings',
                'db_table': 'meteorite_landing',
                'ordering': ['country_area_id', 'meteorite_class_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('planet_id', models.AutoField(primary_key=True, serialize=False)),
                ('planet_name', models.CharField(max_length=50, unique=True)),
                ('unsd_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'UNSD Global World',
                'verbose_name_plural': 'UNSD Global Worlds',
                'db_table': 'planet',
                'ordering': ['planet_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNESCO Region',
                'verbose_name_plural': 'UNESCO Regions',
                'db_table': 'region',
                'ordering': ['region_name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubRegion',
            fields=[
                ('sub_region_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_region_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'UNESCO Sub-Region',
                'verbose_name_plural': 'UNESCO Sub-Regions',
                'db_table': 'sub_region',
                'ordering': ['sub_region_name'],
                'managed': False,
            },
        ),
    ]
