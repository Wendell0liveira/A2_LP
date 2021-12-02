
from django.urls import path
from corrida import views as views

urlpatterns = [
    path("", views.wikipage, name="wikipage"),
    path("wikipage/<str:pagina>", views.wikipage, name="wikipage"),
    path("se_juntar/", views.se_juntar, name="se_juntar"),
    path("redes/<str:rede>", views.redes_sociais, name="redes"),
]
