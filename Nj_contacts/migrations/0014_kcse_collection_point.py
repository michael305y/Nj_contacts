# Generated by Django 4.2.2 on 2023-07-16 16:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nj_contacts', '0013_kepsea_collection_point_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KCSE_collection_point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_code', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_school_code', message='School code should have 8 digits', regex='^20409\\d{3}$')])),
                ('school_name', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_school_name', message='Only letters are allowed', regex="^[A-Za-z\\s.'&-]+$")])),
                ('entry', models.IntegerField()),
                ('collection_point', models.CharField(choices=[('2040901 NJIRU D.C.C’s OFFICE', '2040901 NJIRU D.C.C’s OFFICE'), ("2040902 DANDORA ACC'S OFFICE", "2040902 DANDORA ACC'S OFFICE")], max_length=30)),
                ('route', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]