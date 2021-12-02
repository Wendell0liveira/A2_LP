
from django.urls import path
from pagina_inicial import views as views

urlpatterns = [
    path("index/", views.index, name="index"),
]
