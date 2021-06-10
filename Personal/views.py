#django modules
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#own modules
from Personal.functions import area

def index(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username = email, password = password)

        if user is not None:

            login(request, user)
            
            areas = area(request)

            if areas['area'] == 'Ventas':

                return redirect('Finanzas_sales')

        else:

            context = {'response': 'No existe el usuario, verifique que su usuario y contraseña sean correctos'}

            return render(request, 'index.html', context=context)

    return render(request, 'index.html')

@login_required(login_url='index')
def exit(request):

    logout(request)

    return redirect('index')