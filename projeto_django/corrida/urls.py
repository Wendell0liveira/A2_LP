
from django.urls import path
from corrida import views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:objetivo>/<str:pagina>", views.wikipage, name="wikipage"),
    path("inicio/", views.inicio, name="inicio"),
    path("objetivo/Special:random", views.wikipage, name="comecar")
]
