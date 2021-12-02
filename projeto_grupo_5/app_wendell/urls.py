
from django.urls import path
from app_wendell import views as views

urlpatterns = [
    path("", views.detalhes, name="detalhes"),
    path("detalhes/<str:pagina>", views.detalhes, name="detalhes"),
    path("se_juntar/", views.se_juntar, name="se_juntar"),
    path("redes/<str:rede>", views.redes_sociais, name="redes"),
]
