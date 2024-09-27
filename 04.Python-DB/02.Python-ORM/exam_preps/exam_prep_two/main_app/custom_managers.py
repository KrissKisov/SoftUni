from django.db import models
from django.db.models import QuerySet, Count


class ProfileManager(models.Manager):

    def get_regular_customers(self) -> QuerySet:
        return self.annotate(orders_count=Count("orders_profile"))\
            .filter(orders_count__gt=2)\
            .order_by('-orders_count')