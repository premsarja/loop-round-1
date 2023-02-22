# django imports
from django.utils import timezone

# external imports
import pytz


def local_to_utc(t_stamp, region):
    local_tz = pytz.timezone(region)
