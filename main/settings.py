import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fj@9(_0ecerym9(a=lqv_-@6smmg92^lm3z=02kr@xl7d=4m7i'

LICENSE = 'p67T4splF4DTC++3Bnn0lXwU7najhI+s138vNSUYLJEmAEgZiiXJfrR9nJGfe61Hzff/r8ldJ84ogU5liqoOjHdHCiQk7hDzbbSVV/ufJhg='

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'backend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'djangomako.backends.MakoBackend',
        'NAME': 'mako',
        'DIRS': [
            BASE_DIR + '/backend/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'NAME': 'django',
        'DIRS': [],
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

WSGI_APPLICATION = 'main.wsgi.application'

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kotech_cisco_cms',
        'USER': 'cmsuser',
        'PASSWORD': 'cmsuser',
        'HOST': '182.237.86.248',
        'PORT': '3306',
    }
}

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

DATABASAE_OPTIONS = {'charset':'utf8'}

AUTHORIZATION = 'Basic YWRtaW46RXRlY2hzeXN0ZW0='

#ja = 일본어
#ko = 한국어
#en = 영어
DEFAULT_LANG = 'en'

LANGUAGES = [
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

print(LOCALE_PATHS)

USE_I18N = True
USE_L10N = True
USE_TZ = False

TIME_ZONE = 'Asia/Seoul'

STATIC_ROOT = BASE_DIR + '/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR + '/backend/static/'
]

CORE_APIJSON_PATH = BASE_DIR + '/backend/djangoapps/common/core/api.json'
