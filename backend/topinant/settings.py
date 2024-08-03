import os
from datetime import timedelta
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5=n7$elw!9++%hs2gr@o&#fnp7xk+eb2eoukn+5xc4z4+vwo9c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "djoser",
    "drf_spectacular",
    "user",
    "company",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "topinant.middleware.corsMiddleware.corsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "topinant.urls"

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

WSGI_APPLICATION = "topinant.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

if DEBUG and not bool(os.environ.get("RUN_FROM_DOCKER")):
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # noqa: PTH118
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")  # noqa: PTH118

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.BaseUser"

# rest

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# spectacular

SPECTACULAR_SETTINGS = {
    "TITLE": "Topinant API",
    "DESCRIPTION": "Список всех доступных API запросов",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# djoser

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "https://infoglobal.group/reset-password/{uid}/{token}",
    # "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    # "ACTIVATION_URL": "http://localhost:8080/login/{uid}/{token}",
    # "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    # "SEND_ACTIVATION_EMAIL": False,
    "SEND_CONFIRMATION_EMAIL": False,  # Default False
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": False,  # Default False
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": False,  # Default
    # "LOGOUT_ON_PASSWORD_CHANGE": False,  # Default
    "SERIALIZERS": {
        # "user_create": "user.serializer.UserRegistrationSerializer",  # custom serializer
        # "user": "accounts.serializers.UserMeSetializer",  # custom serializer
        # "current_user": "accounts.serializers.UserMeSetializer",  # custom serializer
        # "user_delete": "user.serializer.UserMeSetializer",  # custom serializer
    },
    # "EMAIL": {
    #     "activation": "accounts.email.ActivationEmail",
    #     "confirmation": "accounts.email.ConfirmationEmail",
    #     "password_reset": "accounts.email.PasswordResetEmail",
    #     "password_changed_confirmation": "accounts.email.PasswordChangedConfirmationEmail",
    # },
}

# JWT

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
#
# cors

CORS_ALLOW_ALL_ORIGINS = True  # разрешить всем
