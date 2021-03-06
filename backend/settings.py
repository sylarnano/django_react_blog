import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS = ['*','0.0.0.0', 'localhost', '127.0.0.1','djanoreact.herokuapp.com']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
  


    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount',
    'rest_framework', 
    'rest_framework.authtoken',
    'corsheaders',

    'contact',
    'blog',
    'comments',

    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "ckeditor"

CKEDITOR_CONFIGS = {
    "default": {
        'toolbar': 'Custom',
        'height': 'auto',
        'width': 'auto',
        # 'skin': 'moono',
        # 'skin': 'kama',
        'toolbar_Custom': [
            ['Bold', '-','Image'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source','codesnippet'],

        ],
       
    },
    'special': {
        'toolbar': 'Special',
        # 'height': 'auto',
        # 'width': 'auto',
        'skin': 'moono',
        'toolbar_Special': [
            ['Bold', 'Image','Link','Unlink', 'CodeSnippet'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['RemoveFormat', 'Source','codesnippet'],


        ],
        'extraPlugins':'codesnippet',
    }

}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'build'],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'build')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

CORS_ALLOW_ALL_ORIGINS = True


REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [

        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [

        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication', # new

        ],

  
}


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
