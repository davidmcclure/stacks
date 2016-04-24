

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^queue/', include('django_rq.urls')),
    url(r'^', include('interface.urls')),
]
