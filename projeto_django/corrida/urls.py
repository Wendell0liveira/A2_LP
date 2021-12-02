
from django.urls import path
from corrida import views as views

urlpatterns = [
    path("wikipage/<str:pagina>", views.wikipage, name="wikipage"),
]
