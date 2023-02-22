# local imports
from .redis import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT

REDIS_Q = {"host": REDIS_HOST, "port": REDIS_PORT, "db": 1, "password": REDIS_PASSWORD}

Q_CLUSTER = {
    "name": "cherry",
    "workers": 4,
    # 'recycle': 500,
    "timeout": 60,
    "retry": 100,
    # 'compress': True,
    # 'save_limit': 250,
    # 'queue_limit': 500,
    # 'cpu_affinity': 1,
    "label": "Django Q",
    "redis": REDIS_Q,
}
