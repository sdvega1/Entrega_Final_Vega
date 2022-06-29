from django.shortcuts import render, HttpResponse
from appVega.models import Fixture, Jugador, Equipo
from appVega.forms import CrearEquipo, CrearFixture, CrearJugador
# Create your views here.
def inicio(request):

    jugadores = Jugador.objects.all()
  

  #    jugadores =  Jugador(nombre="Lionel Messi", nacionalidad="Argentino", edad=35)
   #   jugadores.save()
  #  documentoDeTexto = f"--->Nombre: {jugadores.nombre}   Nacionalidad: {jugadores.nacionalidad}  Edad: {jugadores.edad}"



    return render(request, 'inicio.html', {'jugadores':jugadores})
 
    equipos = Equipo.objects.all()
    return render(request, 'inicio.html', {'equipos':equipos})

def jugadores(request):

    #jugadores = Jugador.objects.all()

    #return render(request, 'jugadores.html', {'jugadores':jugadores})
    def __str__(self):
      return f"Nombre: {self.nombre} - Nacionalidad: {self.nacionalidad} - Edad: {self.edad} - Titulos: {self.titulos} - Equipo: {self.equipo} "


    if request.method =='POST':

        miFormulario = CrearJugador(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          jugador = Jugador(nombre=informacion['nombre'], nacionalidad=informacion['nacionalidad'], edad=informacion['edad'], titulos=informacion['titulos'], equipo=informacion['equipo'])

          jugador.save()

          return render(request, "inicio.html")

    else:
          miFormulario = CrearJugador()
       
    return render(request, 'jugadores.html', {'miFormulario':miFormulario})

def equipos(request):
#    equipos = Equipo.objects.all()

#    return render(request, 'equipos.html', {'equipos':equipos})
    if request.method =='POST':

        miFormulario = CrearEquipo(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          equipo = Equipo(pais=informacion['pais'], titulos=informacion['titulos'])

          equipo.save()

          return render(request, "inicio.html")

    else:
          miFormulario = CrearEquipo()
       
    return render(request, 'equipos.html', {'miFormulario':miFormulario})




def fixture(request):

    #fixture= Fixture.objects.all()

    #return render(request, 'fixture.html', {'fixture':fixture})  

    if request.method =='POST':

        miFormulario = CrearFixture(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
          informacion = miFormulario.cleaned_data
          fixture = Fixture(pais=informacion['pais'], grupo=informacion['grupo'], cabeza_de_serie=informacion['cabeza_de_serie'])

          fixture.save()

          return render(request, "inicio.html")

    else:
          miFormulario = CrearFixture()
       
    return render(request, 'fixture.html', {'miFormulario':miFormulario})


def buscarJugador(request):

   return render(request, 'buscarJugador.html')

def buscar(request):
    #respuesta= f"Estoy buscando al jugador: {request.GET['nombre']}"
    
    if request.GET['nombre']:
      nombre = request.GET['nombre']
      jugadores= Jugador.objects.filter(nombre__icontains=nombre)
    
      return render(request, 'mostrarJugador.html', {'jugadores':jugadores, 'nombre':nombre})

    else:
      
      respuesta = "No enviaste los datos"
    
    return HttpResponse(respuesta)
    #if request.GET['nombre']:
     
     #  jugador = Jugador.objects.filter(nombre__icontains=nombre)
     #  print(jugador)

     #  return render(request,"buscarJugador.html",{"Jugador":jugador.values, "Nombre":nombre})

    #else:
      
    #  respuesta = "No enviaste datos"

    #return render(request, "buscarJugador.html", {"Nombre":respuesta})