from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import *
from assignment.views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('success/', Success.as_view(), name='success'),
    path('admin/', admin.site.urls),
]
