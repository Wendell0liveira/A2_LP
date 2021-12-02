from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path(r"app_wendell/", include("app_wendell.urls")),
    path('admin/', admin.site.urls)
]
