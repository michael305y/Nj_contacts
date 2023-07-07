# Generated by Django 4.2.2 on 2023-07-07 02:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nj_contacts', '0007_remove_contact_email_remove_contact_school_head_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Location',
        ),
        migrations.AlterField(
            model_name='contact',
            name='school_code',
            field=models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_school_code', message='School code should have 8 digits', regex='^20409\\d{3}$')]),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(choices=[('Babadogo', 'Babadogo'), ('Chokaa', 'Chokaa'), ('Dandora', 'Dandora'), ('Dandora phase 1', 'Dandora phase 1'), ('Dandora phase 2', 'Dandora phase 2'), ('Dandora Phase 3', 'Dandora phase 3'), ('Kamulu', 'Kamulu'), ('Kamulu Kipawa', 'Kamulu Kipawa'), ('Kariobangi', 'Kariobangi'), ('Kariobangi South', 'Kariobangi South'), ('Kayole', 'Kayole'), ('Kayole Junction', 'Kayole Junction'), ('Kayole North', 'Kayole North'), ('KCC', 'KCC'), ('Kwa Maji', 'Kwa Maji'), ('Maili Saba', 'Maili Saba'), ('Mihango', 'Mihango'), ('Mowlem', 'Mowlem'), ('Njiru', 'Njiru'), ('Obama', 'Obama'), ('Ruai', 'Ruai'), ('Ruai Block 10', 'Ruai Block 10'), ('Saika', 'Saika'), ('Sewage', 'Sewage'), ('Silanga', 'Silanga'), ('Spring valley', 'Spring valley'), ('Umoja', 'Umoja'), ('Umoja 3', 'Umoja 3'), ('Utawala', 'Utawala'), ('Utawala githunguri', 'Utawala githunguri'), ('other', 'other')], default=True, max_length=30),
            preserve_default=False,
        ),
    ]