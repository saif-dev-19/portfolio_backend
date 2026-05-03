import os
from pathlib import Path

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


def load_local_env():
    env_path = BASE_DIR / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_local_env()


SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-change-me-for-production")
DEBUG = os.environ.get("DEBUG", "True").lower() in {"1", "true", "yes", "on"}


def env_list(name, default=""):
    return [value.strip() for value in os.environ.get(name, default).split(",") if value.strip()]


ALLOWED_HOSTS = env_list(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1,.up.railway.app",
)
railway_public_domain = os.environ.get("RAILWAY_PUBLIC_DOMAIN")
if railway_public_domain and railway_public_domain not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(railway_public_domain)

INSTALLED_APPS = [
    "cloudinary",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "portfolio",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

def valid_env_value(value):
    return value and "USER:PASSWORD@HOST:PORT/DBNAME" not in value and "${{" not in value


database_url = next(
    (
        value
        for value in (
            os.environ.get("DATABASE_URL"),
            os.environ.get("DATABASE_PRIVATE_URL"),
            os.environ.get("DATABASE_PUBLIC_URL"),
        )
        if valid_env_value(value)
    ),
    "",
)
is_railway = any(
    os.environ.get(name)
    for name in ("RAILWAY_ENVIRONMENT", "RAILWAY_PROJECT_ID", "RAILWAY_SERVICE_ID")
)

pg_name = os.environ.get("PGDATABASE") or os.environ.get("POSTGRES_DB") or os.environ.get("POSTGRES_DATABASE")
pg_user = os.environ.get("PGUSER") or os.environ.get("POSTGRES_USER")
pg_password = os.environ.get("PGPASSWORD") or os.environ.get("POSTGRES_PASSWORD")
pg_host = os.environ.get("PGHOST") or os.environ.get("POSTGRES_HOST")
pg_port = os.environ.get("PGPORT", "5432")

if is_railway and not database_url:
    if all([pg_name, pg_user, pg_password, pg_host]):
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": pg_name,
                "USER": pg_user,
                "PASSWORD": pg_password,
                "HOST": pg_host,
                "PORT": pg_port,
                "CONN_MAX_AGE": 600,
                "CONN_HEALTH_CHECKS": True,
            }
        }
    else:
        raise ImproperlyConfigured(
            "PostgreSQL settings are missing. Add DATABASE_URL to the Railway web "
            "service, or add PGDATABASE, PGUSER, PGPASSWORD, PGHOST, and PGPORT. "
            "If you are using Railway variable references, make sure they are saved "
            "on the web service and show resolved values in Railway."
        )
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=database_url or f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
            conn_max_age=600,
            conn_health_checks=True,
        )
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"
        if CLOUDINARY_URL
        else "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
if CLOUDINARY_URL:
    MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS",
    "https://mahfuzur-rahman.vercel.app/",
    "http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174",
)

CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS",
    "http://localhost:5173,http://localhost:5174,http://127.0.0.1:5173,http://127.0.0.1:5174",
    "https://mahfuzur-rahman.vercel.app/",
)

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://localhost:517[0-9]$",
    r"^http://127\.0\.0\.1:517[0-9]$",
    r"^https://.*\.vercel\.app$",
    "https://mahfuzur-rahman.vercel.app/",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}
