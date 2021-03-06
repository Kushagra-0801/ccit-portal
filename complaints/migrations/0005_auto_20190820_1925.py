# Generated by Django 2.2.4 on 2019-08-20 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_auto_20190819_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='handler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handler', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='remark_to_user',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='urgency_reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
