import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='somealosecretkey123',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)



from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.conf.urls import include, re_path


application = get_wsgi_application()

def index(request):
    return HttpResponse("Como Estas?")

urlpatterns = (
    re_path(r'^$', index),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)