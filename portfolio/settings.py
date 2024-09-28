
from pathlib import Path
from environ import Env
import environ
import os
import dj_database_url
import cloudinary
import cloudinary.api
import cloudinary.uploader


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

env = Env()
Env.read_env()



# env = environ.Env()
# environ.Env.read_env() 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!

ENVIRONMENT = env('ENVIRONMENT', default='production')
if ENVIRONMENT == 'development':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'main.apps.MainConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'admin_honeypot',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'compressor',
    'corsheaders',
    
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# POSTGRESQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER': 'postgres',
        'PASSWORD': 'Connectpstgrsqlpdt@6724',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

#AMAZON RDS
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'tportfolio',
#         'USER': 'portfoliopsgr',
#         'PASSWORD': 'Connectamzpsgr6724',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

POSTGRES_LOCCALLY = True
if ENVIRONMENT == 'production' or POSTGRES_LOCCALLY == True:
    DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIR = [BASE_DIR / 'static']
STATICFILES_DIRS = [os.path.join(BASE_DIR / 'static')]

STATIC_ROOT = BASE_DIR / 'staticfiles'


MEDIA_URL = '/media/'

if ENVIRONMENT == 'production' or POSTGRES_LOCCALLY == True:
    # DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    MEDIA_URL = '/media/'
else:
    # Local media storage settings
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print(f"ENVIRONMENT: {ENVIRONMENT}")
print(f"POSTGRES_LOCCALLY: {POSTGRES_LOCCALLY}") 

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('CLOUD_API_KEY'),
    'API_SECRET': env('CLOUD_API_SECRET'),
}

COMPRESS_ENABLED = True
ACCOUNT_USERNAME_BLACKLIST = [ 'admin', 'thepdt' ]



CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',  # Allow all subdomains of onrender.com
    'https://console.cloudinary.com',  # Allow Cloudinary console
]

CORS_ALLOWED_ORIGINS = [
     'https://*.onrender.com',  
    'https://console.cloudinary.com', 
]


# HTTPS settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_REDIRECT = True
SECURE_SSL_REDIRECT = True   # Put True for production
CSRF_COOKIE_SECURE = True

# HSTS settings 
SECURE_HSTS_SECONDS = 31536000 # 1Year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# if ENVIRONMENT == 'production':
#     SECURE_SSL_REDIRECT = True
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
# else:
#     SECURE_SSL_REDIRECT = False
#     SESSION_COOKIE_SECURE = False
#     CSRF_COOKIE_SECURE = False
