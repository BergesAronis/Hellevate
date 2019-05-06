from .settings import *
DEBUG = True
TEMPLATE_DEBUG = True
SECRET_KEY = ')&!2xx+!thhll%)7p_+3*o)y&@y$z(nxbm*em8-wfzu11w_k&('
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hellevate',
        'USER': 'admin',
        'PASSWORD': '1234pass',
        'HOST': 'localhost',
        'PORT': '5432',
        }
}
