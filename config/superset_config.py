import os

from werkzeug.contrib.cache import RedisCache

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')

# Redis Caching variables
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_CACHE_URL = f'redis://{REDIS_HOST}:6379/1'
REDIS_CELERY_URL = f'redis://{REDIS_HOST}:6379/0'

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = os.getenv('SUPERSET_DB')


SUPERSET_WEBSERVER_TIMEOUT = 1810 # same as SQLLAB_TIMEOUT with added buffer

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'super_secret_key_goes_here'
LOG_LEVEL = 'INFO'

# Maximum number of rows returned from a database
# in async mode, no more than SQL_MAX_ROW will be returned and stored
# in the results backend. This also becomes the limit when exporting CSVs
SQL_MAX_ROW = 100000

# Default row limit for SQL Lab queries
DEFAULT_SQLLAB_LIMIT = 250

# Maximum number of tables/views displayed in the dropdown window in SQL Lab.
MAX_TABLE_NAMES = 3000

# Timeout duration for SQL Lab synchronous queries
SQLLAB_TIMEOUT = 120 

SUPERSET_WEBSERVER_TIMEOUT = 300
# The MAX duration (in seconds) a query can run for before being killed
# by celery.
SQLLAB_ASYNC_TIME_LIMIT_SEC = 60 * 60 * 2 # 2 hours max for async

RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=6379,
    key_prefix='superset_results'
)

CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': REDIS_CACHE_URL}

class CeleryConfig(object):
    BROKER_URL = REDIS_CELERY_URL
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = REDIS_CACHE_URL
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '100/s'}}
    CELERYD_LOG_LEVEL = 'DEBUG'
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_TASK_PROTOCOL = 1
    CELERY_ACKS_LATE = True

CELERY_CONFIG = CeleryConfig
