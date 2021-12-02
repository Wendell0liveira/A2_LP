from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path(r"corrida/", include("corrida.urls")),
    path(r"pagina_inicial/", include("pagina_inicial.urls")),
    path('admin/', admin.site.urls)
]
