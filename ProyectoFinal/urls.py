from django.contrib import admin
from django.urls import path, include
from AppLab.views import tramites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppLab/', include('AppLab.urls')),
]
