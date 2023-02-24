# python imports
import binascii
import os

# django imports
from django.utils import timezone

# external imports
import pytz


def local_to_utc(t_stamp, region):
    local_tz = pytz.timezone(region)


def generate_key():
    return binascii.hexlify(os.urandom(10)).decode()
