
from django.urls import path
from corrida import views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("inicio/<str:modo>", views.inicio, name="inicio"),
    path("<str:objetivo>/<str:pagina>", views.wikipage, name="wikipage"),
    path("objetivo/Special:random", views.wikipage, name="comecar"),
    path("mododejogo", views.mododejogo, name="mododejogo"),
    
]
