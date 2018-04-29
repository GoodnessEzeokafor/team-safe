# Generated by Django 2.0.4 on 2018-04-26 11:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nature Of Incidence', max_length=200)),
                ('description', models.TextField(help_text='Write a description')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_0', models.BigIntegerField(default=1)),
                ('iso', models.CharField(max_length=3)),
                ('name_0', models.CharField(max_length=75)),
                ('id_1', models.BigIntegerField(default=1)),
                ('name_1', models.CharField(max_length=75)),
                ('hasc_1', models.CharField(max_length=15)),
                ('ccn_1', models.BigIntegerField(default=1)),
                ('cca_1', models.CharField(max_length=254)),
                ('type_1', models.CharField(max_length=50)),
                ('engtype_1', models.CharField(max_length=50)),
                ('nl_name_1', models.CharField(max_length=50)),
                ('varname_1', models.CharField(max_length=150)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]