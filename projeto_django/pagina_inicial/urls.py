
from django.urls import path
from pagina_inicial import views as views
from corrida import views as views_corrida
urlpatterns = [
    path("index/", views.index, name="index"),
    path("inicio/",views_corrida.inicio,name="inicio")
]
