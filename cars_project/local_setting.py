
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fu3x!7chc*q$*@j7*$=q4olfqu)r&$pe56zw4c&@l6x3hi(&bi'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Football1!'
    }
}