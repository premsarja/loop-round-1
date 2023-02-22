# django imports
from django.db import models

class Store(models.Model):
    store_id = models.PositiveBigIntegerField(primary_key=True, db_index=True)
    time_zone_str = models.CharField(max_length=50)

    class Meta:
        db_table = "store"


class StoreStatus(models.Model):
    STATUS_CHOICES = (("active", "active"), ("inactive", "inactive"))

    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "store_status"


class StoreHours(models.Model):
    class DOW(models.IntegerChoices):
        MONDAY = 0
        TUESDAY = 1
        WEDNESDAY = 2
        THURSDAY = 3
        FRIDAY = 4
        SATURDAY = 5
        SUNDAY = 6

    store = models.ForeignKey(to=Store, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=DOW.choices)
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

    class Meta:
        db_table = "store_hours"
