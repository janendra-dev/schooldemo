

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4b*0k#rdr_2kruwx(+ffe&)!&3j4jbkw5(=fm+zjc@b8^lj4@l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# setting media and static
MEDIA_URL="/media/"
MEDIA_ROOT=Path(BASE_DIR,"media")

STATIC_URL="/static/"
STATIC_ROOT=Path(BASE_DIR,"static")
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'schoolapp',
    'django.contrib.sites',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'schoolapp.LoginCheckMiddleWare.LoginCheckMiddleWare',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
]
SITE_ID=1
ROOT_URLCONF = 'dschool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [ Path(BASE_DIR, 'schoolapp/template'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# Static files (CSS, JavaScript, Imag
STATIC_URL = '/static/'

AUTH_USER_MODEL="schoolapp.CustomUser"

AUTHENTICATION_BACKENDS=["django.contrib.auth.backends.ModelBackend",
                            'allauth.account.auth_backends.AuthenticationBackend',
                            'schoolapp.EmailBackEnd.EmailBackEnd',
                            ]

EMAIL_BACKEND="django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH=Path(BASE_DIR,"sent_mails")

# EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST="smtp.gmail.com"
# EMAIl_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER="janendrakawar123@gmail.com"
# EMAIL_HOST_PASSWORD="jkyksk1@1"
# DEFAULT_FROM_EMAIL="backend<webmaster@my-host.com>"


#Enable Only Making Project Live on Heroku
# STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
# import dj_database_url
# prod_db=dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)

