import environ
import os
from pathlib import Path

# Definir BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Inicializar `environ`
env = environ.Env(
    DEBUG=(bool, False)
)

# Leer el archivo .env si existe
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Configuración rápida para desarrollo - no adecuado para producción
# Ver https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# ¡ADVERTENCIA DE SEGURIDAD: mantén la clave secreta usada en producción en secreto!
SECRET_KEY = env('p3&$kke+-o30rm64$f0wfzd5m73zssi9$)%89*7hxwg8917d)*', default='django-insecure-3wgh$7&ehk%w7@19g=dobp_^k$_^p#5jddm#)+k2&iz8n(*gnf')

# ¡ADVERTENCIA DE SEGURIDAD: no ejecutes con debug activado en producción!
DEBUG = env('DEBUG', default=False)

# Definir los hosts permitidos
ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

# Definición de aplicaciones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'registroPersonas',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_countries',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'losLirios.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Configuración de WSGI
WSGI_APPLICATION = 'losLirios.wsgi.application'

# Configuración de la base de datos
# Ver https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite3')
}

# Validación de contraseñas
# Ver https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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

# Internacionalización
# Ver https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, Imágenes)
# Ver https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Definición de tipo de campo de clave primaria por defecto
# Ver https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de autenticación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Configuración de django-allauth
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = True

# Redirección de inicio de sesión y cierre de sesión
LOGIN_REDIRECT_URL = '/usuarios/bienvenida/'
LOGOUT_REDIRECT_URL = '/'
