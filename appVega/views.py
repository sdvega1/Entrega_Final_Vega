from cmath import log
from pickle import TRUE
from urllib import request
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from platformdirs import user_log_dir
from appVega.models import Blog, Fixture, Jugador, Equipo, Avatar
from appVega.forms import CrearEquipo, CrearFixture, CrearJugador, UserEditForm, UserRegisterForm, CrearBlog
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
#def avatar(request):
#      avatares = Avatar.objects.filter(user=request.user.id)
#      return render(request, "inicio.html", {"url": avatares[0].imagen.url} )     

def busc_avatar_url(user):
      avatares=Avatar.object.filter(user=request.user.id)
      if avatares.exist():
            return avatares.first().imagen.url
      return None

def inicio(request):

    jugadores = Jugador.objects.all()
    equipos = Equipo.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if  request.user.is_authenticated:

            return render(request, 'inicio.html', {'jugadores':jugadores,'equipos':equipos, "url": avatares[0].imagen.url })
            
            
    else:

            return render(request, 'inicio.html')
            

   # return render(request, 'inicio.html', {'jugadores':jugadores,'equipos':equipos, "url": avatares[0].imagen.url })
 
 

def jugadores(request):

    if request.method =='POST':

        miFormulario = CrearJugador(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          jugador = Jugador(nombre=informacion['nombre'], nacionalidad=informacion['nacionalidad'], edad=informacion['edad'], titulos=informacion['titulos'], equipo=informacion['equipo'])

          jugador.save()
          avatares = Avatar.objects.filter(user=request.user.id) 
          return render(request, "inicio.html", {"url": avatares[0].imagen.url})

    else:
          miFormulario = CrearJugador()
          avatares = Avatar.objects.filter(user=request.user.id)   
    return render(request, 'jugadores.html', {'miFormulario':miFormulario, "url": avatares[0].imagen.url})

@login_required
def equipos(request):
    avatares = Avatar.objects.filter(user=request.user.id)  
    if request.method =='POST':

        miFormulario = CrearEquipo(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          equipo = Equipo(pais=informacion['pais'], titulos=informacion['titulos'])

          equipo.save()

          return render(request, "inicio.html", {"url": avatares[0].imagen.url})

    else:
          miFormulario = CrearEquipo()
       
    return render(request, 'equipos.html', {'miFormulario':miFormulario,"url": avatares[0].imagen.url})




def fixture(request):
    avatares = Avatar.objects.filter(user=request.user.id)  
    fixture= Fixture.objects.all()
    if  request.user.is_authenticated:
      return render(request, 'fixture.html', {'fixture':fixture, "url": avatares[0].imagen.url })  
    else:
      return render(request, 'fixture.html', {'fixture':fixture})

 #   if request.method =='POST':
#
#        miFormulario = CrearFixture(request.POST)

#        print(miFormulario)

#        if miFormulario.is_valid:
#          informacion = miFormulario.cleaned_data
#          fixture = Fixture(pais=informacion['pais'], grupo=informacion['grupo'], cabeza_de_serie=informacion['cabeza_de_serie'])

#          fixture.save()

#          return render(request, "inicio.html")

#    else:
#          miFormulario = CrearFixture()
       
#    return render(request, 'fixture.html', {'miFormulario':miFormulario})

@login_required
def blog (request):
    avatares = Avatar.objects.filter(user=request.user.id)  
    if request.method =='POST':

        miFormulario = CrearBlog(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          blog = Blog(nombre=informacion['nombre'], titulo=informacion['titulo'], fecha=informacion['fecha'], cuerpo=informacion['cuerpo'])

          blog.save()

          contexto = {"blog":blog}
           
 
          return render(request, 'ver_blogs.html', contexto) 

    else:
          miFormulario = CrearBlog()
       
    return render(request, 'blogs.html', {'miFormulario':miFormulario, "url": avatares[0].imagen.url})


def buscarJugador(request):
   avatares = Avatar.objects.filter(user=request.user.id)  
   
   if  request.user.is_authenticated:
      return render(request, 'buscarJugador.html', {"url": avatares[0].imagen.url})
   else:
      return render(request, 'buscarJugador.html' )

def buscar(request):
    #respuesta= f"Estoy buscando al jugador: {request.GET['nombre']}"
    avatares = Avatar.objects.filter(user=request.user.id)  
    if request.GET['nombre']:
      nombre = request.GET['nombre']
      jugadores= Jugador.objects.filter(nombre__icontains=nombre)
      
      if  request.user.is_authenticated:
            return render(request, 'mostrarJugador.html', {'jugadores':jugadores, 'nombre':nombre, "url": avatares[0].imagen.url})
      else:
            return render(request, 'mostrarJugador.html', {'jugadores':jugadores, 'nombre':nombre })

    else:
      
      respuesta = "No enviaste los datos"
    
    return HttpResponse(respuesta)
   
def listados(request):
  avatares = Avatar.objects.filter(user=request.user.id) 
  jugadores = Jugador.objects.all()


  if  request.user.is_authenticated:
      return render(request, 'listados.html', {'jugadores':jugadores, "url": avatares[0].imagen.url})
  else:
      return render(request, 'listados.html', {'jugadores':jugadores})

def listEquipos(request):
        avatares = Avatar.objects.filter(user=request.user.id) 
        equipos = Equipo.objects.all()
        
        if  request.user.is_authenticated:
            return render(request, 'listEquipos.html', {'equipos':equipos, "url": avatares[0].imagen.url}) 
        else:
            return render(request, 'listEquipos.html', {'equipos':equipos })

def about(request):
  avatares = Avatar.objects.filter(user=request.user.id)
  if  request.user.is_authenticated:
      return render(request, 'about.html', {"url": avatares[0].imagen.url})
  else:
      return render(request, 'about.html')

@login_required
def eliminarJugador(request, jugador_nombre):
  avatares = Avatar.objects.filter(user=request.user.id)  
  jugador = Jugador.objects.get(nombre=jugador_nombre)
  
  jugador.delete()

  jugadores = Jugador.objects.all()

  contexto = {"jugadores":jugadores, "url": avatares[0].imagen.url}

  return render(request, "listados.html", contexto)

@login_required
def editarJugador(request, jugador_nombre):
      avatares = Avatar.objects.filter(user=request.user.id)  
      jugador = Jugador.objects.get(nombre= jugador_nombre)
  
      if request.method == 'POST':

            miFormulario = CrearJugador(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  jugador.nombre =informacion['nombre']
                  jugador.nacionalidad = informacion['nacionalidad']
                  jugador.edad = informacion['edad']
                  jugador.equipo = informacion['equipo']
                  jugador.titulos = informacion['titulos']

                  jugador.save()
                  if  request.user.is_authenticated:
                        return render(request, 'listados.html', {"url": avatares[0].imagen.url})
                  else:
                        return render(request, 'listados.html')

      else:

            miFormulario = CrearJugador(initial={'nombre':jugador.nombre, 'nacionalidad':jugador.nacionalidad, 'edad':jugador.edad, 'equipo':jugador.equipo, 'titulos':jugador.titulos })
      
      if  request.user.is_authenticated:
            return render(request, 'editarJugador.html', {'miFormulario':miFormulario,'jugador_nombre':jugador_nombre, "url": avatares[0].imagen.url })
      else:
            return render(request, 'editarJugador.html', {'miFormulario':miFormulario,'jugador_nombre':jugador_nombre })

def verJugador(request, jugador_nombre):
  avatares = Avatar.objects.filter(user=request.user.id)  
  jugadores = Jugador.objects.get(nombre=jugador_nombre)
 
  



  if  request.user.is_authenticated:
      contexto = {'jugadores':jugadores, "url": avatares[0].imagen.url}
      return render(request, 'verJugador.html',contexto)

  else:
      contexto1 = {'jugadores':jugadores}
      return render(request, 'verJugador.html',contexto1)



def ver_blogs(request):
  avatares = Avatar.objects.filter(user=request.user.id)
  blogs = Blog.objects.all()
  
  if  request.user.is_authenticated:
      return render(request, 'ver_blogs.html', {'blogs':blogs, "url": avatares[0].imagen.url}) 
  else:
      return render(request, 'ver_blogs.html', {'blogs':blogs})


class JugadorList(LoginRequiredMixin, ListView):

    model = Jugador
    template_name = 'jugadores_list.html'

class JugadorDetalle(DetailView):

      model = Jugador
      template_name = "jugador_detalle.html"



class JugadorCreacion(LoginRequiredMixin, CreateView):

      model = Jugador
      template_name = "jugador_form.html"
      fields = ['nombre', 'nacionalidad', 'edad', 'equipo', 'titulos']
      success_url=reverse_lazy('Listados')

class JugadorUpdate(UpdateView):

      model = Jugador
      template_name = "jugador_form.html"
      fields  = ['nombre', 'nacionalidad', 'edad', 'equipo', 'titulos']
      success_url=reverse_lazy('List')

class JugadorDelete(DeleteView):
      model = Jugador
      success_url = '/jugador/list'

def login_request(request):
      #capturamos el post
 
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "registro.html", {"form": form})


@login_required
def editarPerfil(request):
      #se instancia el Login;
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.first_name = informacion['first_name']
                  usuario.last_name = informacion['last_name']
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

