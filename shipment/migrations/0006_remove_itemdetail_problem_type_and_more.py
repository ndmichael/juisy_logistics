# Generated by Django 4.0.6 on 2022-08-13 15:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0005_alter_itemdetail_date_shipped_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdetail',
            name='problem_type',
        ),
        migrations.RemoveField(
            model_name='itemdetail',
            name='status',
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='date_shipped',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 14, 15, 55, 32, 936851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 20, 15, 55, 32, 936851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdetail',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='itemreciever',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='itemsender',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('transit', 'ON TRANSIT'), ('withheld', 'WITHHELD'), ('sent', 'SENT'), ('delivered', 'DELIVERED')], default='transit', max_length=15)),
                ('problem_type', models.CharField(choices=[('no problem', 'No Problems'), ('paperwork', 'PAPERWORK_OVERLOAD'), ('custom clerance', 'CUSTOM CLEARANCE'), ('bad weather', 'BAD WEATHER')], default='no problem', max_length=15)),
                ('country', django_countries.fields.CountryField(max_length=50)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_status', to='shipment.itemdetail')),
            ],
        ),
    ]
