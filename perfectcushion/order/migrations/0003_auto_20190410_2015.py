# Generated by Django 2.1.4 on 2019-04-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190410_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shippingAddress1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingCity',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingCountry',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingName',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingPostCode',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
