from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from primerProyecto.forms import LoginForm


def login_page(request):
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Te has identificado de modo correcto"
                else:
                    message = "Tu usuario esta inactivo"
            else:
                message = "Nombre de usuario y/o password incorrecto"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'message': message, 'form': form})


def homepage(request):
    return render(request, 'homepage.html')


def logout_view(request):
    logout(request)
    return redirect('homepage')