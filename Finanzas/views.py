#django modules
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#own modules
from Personal.functions import area

@login_required(login_url='index')
def sales(request):

    context = area(request)

    return render(request, 'Finanzas_sales.html', context= context)