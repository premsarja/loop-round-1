# python imports
import csv

# django imports
from django.utils import timezone

# external imports
from store.models import Store, StoreHours, StoreStatus

# bulk load store id & timezone to db
# with open("./inputs/store-zone.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader, None)
#     store = [Store(store_id=row[0], time_zone_str=row[1]) for row in reader]
#     Store.objects.bulk_create(store)

# # load store hours to db
# with open("./inputs/store-hours.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader, None)
#     for row in reader:
#         try:
#             StoreHours.objects.create(store_id=row[0],day_of_week=row[1],start_time_local=row[2],end_time_local=row[3])
#         except:
#             Store.objects.create(store_id=row[0], time_zone_str="America/Chicago")
#             StoreHours.objects.create(store_id=row[0],day_of_week=row[1],start_time_local=row[2],end_time_local=row[3])

# # find store ids not in store-zone and create store zone records
# with (
#     open("./inputs/store-zone.csv", "r") as f1,
#     open("./inputs/store-hours.csv", "r") as f2,
#     open("./inputs/store-status.csv", "r") as f3
# ):
#     ssl = []
#     sl = []
#     fl = []

#     r1 = csv.reader(f1)
#     next(r1, None)
#     for row in r1:
#         ssl.append(row[0])
#         sl.append(row[0])

#     r2 = csv.reader(f2)
#     next(r2, None)
#     for row in r2:
#         ssl.append(row[0])
#         sl.append(row[0])

#     r3 = csv.reader(f3)
#     next(r3, None)
#     for row in r3:
#         ssl.append(row[0])

#     ssl = list(set(ssl))
#     sl = list(set(sl))
#     for i in ssl:
#         if i not in sl:
#             fl.append(i)

#     store = [Store(store_id=i, time_zone_str="America/Chicago") for i in fl]
#     Store.objects.bulk_create(store)

# # bulk load status and timestamp to db
# with open("./inputs/store-status.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader, None)
#     store_status = [
#         StoreStatus(
#             store_id=row[0],
#             status=row[1],
#             timestamp=row[2].replace(" UTC", "+00:00")
#         ) for row in reader]
#     StoreStatus.objects.bulk_create(store_status, batch_size=1000)
