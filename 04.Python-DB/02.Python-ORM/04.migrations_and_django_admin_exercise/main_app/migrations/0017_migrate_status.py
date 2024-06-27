# Generated by Django 5.0.4 on 2024-06-27 22:35

from django.db import migrations
from django.utils import timezone


def set_status(apps, schema_editor):

    order_model = apps.get_model('main_app', 'Order')

    orders = order_model.objects.all()

    for order in orders:

        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
            order.save()

        elif order.status == 'Completed':
            order.warranty = '24 months'
            order.save()

        elif order.status == 'Cancelled':
            order.delete()


def set_reversed_status(apps, schema_editor):

    order_model = apps.get_model('main_app', 'Order')

    orders = order_model.objects.all()

    for order in orders:
        if order.status == "Pending":
            order.delivery = None

        elif order.status == "Completed":
            order.warranty = order_model._meta.get_field('warranty').default

    order_model.objects.bulk_update(orders, ['delivery', 'warranty'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_order'),
    ]

    operations = [
        migrations.RunPython(set_status, set_reversed_status)
    ]
