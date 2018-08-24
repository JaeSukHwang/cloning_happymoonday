# Generated by Django 2.0.7 on 2018-08-22 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_for_Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='img',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='order',
        ),
        migrations.AddField(
            model_name='goods',
            name='img_back',
            field=models.ImageField(blank=True, upload_to='store/'),
        ),
        migrations.AddField(
            model_name='goods',
            name='img_front',
            field=models.ImageField(blank=True, upload_to='store/'),
        ),
        migrations.AddField(
            model_name='goods',
            name='img_inner',
            field=models.ImageField(blank=True, upload_to='store/'),
        ),
        migrations.AddField(
            model_name='goods',
            name='img_side',
            field=models.ImageField(blank=True, upload_to='store/'),
        ),
        migrations.AddField(
            model_name='cart_for_goods',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods'),
        ),
    ]
