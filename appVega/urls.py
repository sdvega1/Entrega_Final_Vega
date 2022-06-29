from django.urls import path

from appVega import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('fixture', views.fixture, name="Fixture"),
 #   path('crearForm', views.crearForm, name="CrearForm"),
    path('buscarJugador', views.buscarJugador, name="BuscarJugador"),
    path('buscar/', views.buscar),
    path('buscar/', views.buscar),

]