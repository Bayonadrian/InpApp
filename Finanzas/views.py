#django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
#python modules
import os
#third party-modules
#own modules
from Personal.functions import area
from Finanzas.forms import SalesForm, Sales

@login_required(login_url='index')
def sales(request):

    form = SalesForm()

    context = area(request)

    if request.method == 'POST':

        typeOf = ""

        if request.POST['company'] == True:

            typeOf = 'Empresa'
        
        else:

            typeOf = 'Particular'

        data = {
            'document': request.POST['document'],
            'company': typeOf,
            'vendor': request.user,
            'name': request.POST['name'],
            'address': request.POST['address'],
            'district': request.POST['district'],
            'department': request.POST['department'],
            'refference': request.POST['refference'],
            'speed': request.POST['speed'],
            'province': request.POST['province'],
            'payment': request.POST['payment'],
            'toPay': request.POST['toPay'],
            'ip': request.POST['ip'],
            'phone': request.POST['phone'],
            'mail': request.POST['mail'],
            'observations': request.POST['observations'],
            'priority': request.POST['priority'],
            'service': request.POST['service'],
            'install_date': request.POST['install_date'],
            'materials': request.POST['materials'],
            'price': request.POST['price'],
        }

        form = SalesForm(data)

        if form.is_valid():

            form.save()

            sale = Sales.objects.get(document = request.POST['document'])

            if typeOf == 'Particular':

                path = os.path.realpath('Finanzas/pdfDocs/Particular/Contract.html')

                with open(path, 'r') as doc:

                    document = doc.read().format(
                    id = sale.id,
                    date = timezone.datetime.today().year,
                    sr = sale.name,
                    address = sale.address,
                    district = sale.district,
                    province = sale.province,
                    department = sale.department,
                    dni = sale.document,
                    phone = sale.phone,
                    email = sale.mail,
                    day = timezone.datetime.today().day,
                    month = timezone.datetime.today().month,
                    year = timezone.datetime.today().year,
                    lastDay = timezone.datetime.today().day,
                    lastMonth = timezone.datetime.today().month,
                    lastYear = timezone.datetime.today().year+1,
                    cost = sale.price,
                    mb = sale.speed,
                    montly = sale.toPay,
                    todayDay = timezone.datetime.today().day,
                    todayMonth = timezone.datetime.today().month,
                    todayYear = timezone.datetime.today().year,
                    client = sale.name
                    )

                    response = HttpResponse(document, content_type='application/html')
                    response['Content-Disposition'] = 'inline; filename="Contract{}-{}.html"'.format(sale.id, timezone.datetime.today())

                return response

            else:

                pass

        else:

            context = area(request, response = form.errors)

            return render(request, 'Finanzas_sales.html', context= context)

    return render(request, 'Finanzas_sales.html', context= context)

@login_required(login_url='index')
def todaysAbstract(request):

    abstract = Sales.objects.filter(date__day=timezone.datetime.today().day)

    context = area(request, abstract=abstract)

    return render(request, 'Finanzas_todaysAbstract.html', context=context)