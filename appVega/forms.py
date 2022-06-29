from django import forms

class CrearJugador(forms.Form):

    nombre=forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=20)
    edad=forms.IntegerField()
    titulos = forms.IntegerField()
    #foto=ImageField(upload_to='appVega/fotos')
    equipo=forms.CharField(max_length=40)    

class CrearEquipo(forms.Form):

    pais=forms.CharField(max_length=20)
    titulos=forms.IntegerField()


class CrearFixture(forms.Form):
    pais=forms.CharField(max_length=20)
    grupo=forms.CharField(max_length=20)
    cabeza_de_serie=forms.BooleanField()