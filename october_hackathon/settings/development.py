from .base import *
SECRET_KEY = "django-insecure-seaj4)@+hm=r=gl-1bpg#(7iz%7tfux1qv@ubd6(y_sv$fw@xn"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}