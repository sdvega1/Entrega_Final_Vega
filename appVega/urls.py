from django.urls import path

from appVega import views
from django.contrib.auth.views import LogoutView
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('fixture', views.fixture, name="Fixture"),
    path('blog', views.blog, name="Blog"),
    path('ver_blogs', views.ver_blogs, name="Ver_Blogs"),    
 #   path('crearForm', views.crearForm, name="CrearForm"),
    path('buscarJugador', views.buscarJugador, name="BuscarJugador"),
    path('buscar/', views.buscar),
    path('listados/', views.listados, name="Listados"),
    path('listEquipos/', views.listEquipos, name="ListadoEquipos"),
    path('about', views.about, name="About"),
    path('eliminarJugador/<jugador_nombre>/', views.eliminarJugador, name="EliminarJugador"),
    path('editarJugador/<jugador_nombre>/', views.editarJugador, name="EditarJugador"),
    path('verJugador/<jugador_nombre>/', views.verJugador, name="VerJugador"),
    path('jugador/list', views.JugadorList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.JugadorDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.JugadorCreacion.as_view(), name='New'),
    #path('nuevo/', views.JugadorCreacion.as_view(), name='New'),
    re_path(r'^editar/(?P<pk>\d+)$', views.JugadorUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.JugadorDelete.as_view(), name='Delete'),   
    path('login', views.login_request, name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register', views.register, name='register'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)