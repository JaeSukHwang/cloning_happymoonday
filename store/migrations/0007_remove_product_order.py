# Generated by Django 2.0.7 on 2018-08-08 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20180803_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
    ]
