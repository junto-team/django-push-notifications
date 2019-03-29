# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0006_webpushdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcmdevice',
            name='device_id',
            field=models.TextField(blank=True, db_index=True, help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', null=True, verbose_name='Device ID'),
        ),
    ]
