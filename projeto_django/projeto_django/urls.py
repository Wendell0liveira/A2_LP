from django.contrib import admin
from django.urls import path,include
from corrida.views import index
from register import views as register_views
urlpatterns = [
    path("",index,name='pagina inicial'),
    path("register/", register_views.register, name="register"),
    path(r"corrida/", include("corrida.urls")),
    path('admin/', admin.site.urls)
]
