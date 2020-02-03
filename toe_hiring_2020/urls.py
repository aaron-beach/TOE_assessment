from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('assignment/', include('assignment.urls')),
    path('admin/', admin.site.urls),
]
