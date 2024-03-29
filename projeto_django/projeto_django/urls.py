from django.contrib import admin
from django.urls import path,include
from corrida.views import index
from corrida.views import analises
from register import views as register_views
urlpatterns = [
    path("analises/",analises,name='analises'),
    path("",index,name='pagina inicial'),
    path("index/",index,name='pagina inicial'),
    path("login/index/",index,name='pagina inicial'),
    path("logout/index/",index,name='pagina inicial'),
    path("register/", register_views.register, name="register"),
    path(r"corrida/", include("corrida.urls")),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")), 
]
