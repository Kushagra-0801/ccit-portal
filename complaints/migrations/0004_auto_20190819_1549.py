# Generated by Django 2.2.4 on 2019-08-19 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_auto_20190818_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='contact_no',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number is not in the correct format.', regex='^(\\+?91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='unblockrequest',
            name='url',
            field=models.TextField(error_messages={'unique': 'This url is already under consideration'}, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
