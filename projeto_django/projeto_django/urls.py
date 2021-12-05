from django.contrib import admin
from django.urls import path,include
from corrida.views import index
urlpatterns = [
    path("",index,name='pagina inicial'),
    path(r"corrida/", include("corrida.urls")),
    path('admin/', admin.site.urls)
]
