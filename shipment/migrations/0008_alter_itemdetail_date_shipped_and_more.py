# Generated by Django 4.0.6 on 2022-08-16 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0007_rename_item_reciever_itemdetail_item_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='date_shipped',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 17, 19, 24, 53, 444471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 23, 19, 24, 53, 444471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='item_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='weight',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='status',
            name='problem_type',
            field=models.CharField(choices=[('no problem', 'No Problems'), ('paperwork', 'PAPERWORK_OVERLOAD'), ('custom clerance', 'CUSTOM CLEARANCE'), ('bad weather', 'BAD WEATHER')], default='no problem', max_length=100),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('transit', 'ON TRANSIT'), ('withheld', 'WITHHELD'), ('sent', 'SENT'), ('delivered', 'DELIVERED')], default='transit', max_length=100),
        ),
    ]
