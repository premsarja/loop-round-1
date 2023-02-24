# python imports
import csv
import time

# django imports
from django.conf import settings
from django.db import connection

# local imports
from .raw_sql import report_part_1


def generate_report(*args, **kwargs):
    filename = kwargs.get("filename")
    file_path = settings.BASE_DIR.joinpath(f"store/export/{filename}.csv")
    data = []

    with connection.cursor() as cursor:
        cursor.execute(sql=report_part_1)
        context = cursor.fetchall()
        for i in context:
            data.append(i)

    with open(file_path, "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "store_id",
                "timezone",
                "status",
                "timestamp",
                "day_of_week",
                "start_time",
                "end_time",
            )
        )
        for row in data:
            writer.writerow(row)
