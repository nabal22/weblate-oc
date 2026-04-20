import os
from weblate.settings_example import *  # noqa

SECRET_KEY = os.environ["WEBLATE_SECRET_KEY"]
DEBUG = False
ALLOWED_HOSTS = os.environ.get("WEBLATE_ALLOWED_HOSTS", "*").split(",")
SITE_DOMAIN = os.environ["WEBLATE_SITE_DOMAIN"]
SITE_TITLE = os.environ.get("WEBLATE_SITE_TITLE", "Weblate")
ENABLE_HTTPS = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRESQL_ADDON_DB"],
        "USER": os.environ["POSTGRESQL_ADDON_USER"],
        "PASSWORD": os.environ["POSTGRESQL_ADDON_PASSWORD"],
        "HOST": os.environ["POSTGRESQL_ADDON_HOST"],
        "PORT": os.environ["POSTGRESQL_ADDON_PORT"],
        "CONN_MAX_AGE": 60,
        "OPTIONS": {"sslmode": "require"},
    }
}

REDIS_URL = (
    f"redis://:{os.environ['REDIS_PASSWORD']}"
    f"@{os.environ['REDIS_HOST']}:{os.environ['REDIS_PORT']}/0"
)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "weblate",
    },
    "avatar": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": os.path.join(os.environ.get("DATA_DIR", "/tmp/weblate"), "avatar-cache"),
        "TIMEOUT": 86400,
    },
}

CELERY_TASK_ALWAYS_EAGER = False
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

DATA_DIR = os.environ.get("DATA_DIR", "/weblate-data")
STATIC_ROOT = os.path.join(os.path.dirname(__file__), "static")

EMAIL_HOST = os.environ.get("WEBLATE_EMAIL_HOST", "")
EMAIL_HOST_USER = os.environ.get("WEBLATE_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("WEBLATE_EMAIL_HOST_PASSWORD", "")
EMAIL_PORT = int(os.environ.get("WEBLATE_EMAIL_PORT", "587"))
EMAIL_USE_TLS = True
SERVER_EMAIL = os.environ.get("WEBLATE_SERVER_EMAIL", "weblate@example.com")
DEFAULT_FROM_EMAIL = SERVER_EMAIL
