# Generated by Django 2.0.7 on 2018-07-29 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_manufac_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
