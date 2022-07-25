from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CrearBlog(forms.Form):
    nombre=forms.CharField(max_length=20)
    titulo=forms.CharField(max_length=30)
    fecha=forms.DateField()
    cuerpo=forms.CharField(max_length=500)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}