# Generated by Django 2.1.3 on 2018-11-21 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20181121_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
