from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Login personalizado turismo
def login_turismo(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print('POST *******')
        if form.is_valid():
            usuario = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=usuario, password=password)

            # Validamos que las credenciales coincidan y devuelva un user
            if user is not None:
                print('Coincidencia! Logueando')
                login(request,user)
                messages.success(request, f'Logueado como {usuario}')
                return redirect('usuarios:index')
            else:
                messages.error(request, f'Usuario o password incorrecto')
        else:
            messages.error(request, f'Datos erróneos')

    form = AuthenticationForm()
    return render(request,'registration/login.html', {'form':form})



