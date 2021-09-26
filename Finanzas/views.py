#django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
#python modules
import os.path
#third party-modules
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
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
            'refference': request.POST['refference'],
            'speed': request.POST['speed'],
            'province': request.POST['province'],
            'payment': request.POST['payment'],
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

            w, h = A4

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'

            pdf = canvas.Canvas(response, pagesize =A4)
            pdf.setFont('Helvetica-Bold', 14)
            pdf.drawString((w/2)-150, h-20, 'Contrato de prestacion de servicios N° {num} - {date}'.format(num= sale.id, date=timezone.datetime.today().year))
            pdf.setFont('Helvetica', 14)

            # find and read

            path = os.path.realpath('Finanzas/pdfMk/Company/companyContract.md')

            with open(path, 'r') as companyContract:

                imgPath = os.path.realpath('static/images/logo.png')

                logo =  ImageReader(imgPath)

                pdf.drawImage(logo, (w/2)-170, h-350)
                pdf.drawString(30, h-50, companyContract.readline(62))
                pdf.drawString(30, h-70, companyContract.readline(62))
                pdf.drawString(30, h-90, companyContract.readline(62))
                pdf.drawString(30, h-110, companyContract.readline(62))
                pdf.drawString(30, h-130, companyContract.readline(62))
                pdf.drawString(30, h-150, companyContract.readline(62))
                pdf.drawString(30, h-170, companyContract.readline(62))
                pdf.drawString(30, h-190, companyContract.readline(62))
                pdf.drawString(30, h-210, companyContract.readline(62))
                pdf.drawString(30, h-230, companyContract.readline(36))
                pdf.drawString(30, h-250, companyContract.readline(3).format(sale.name))
                pdf.drawString(30, h-270, companyContract.readline(10))
                pdf.drawString(30, h-290, companyContract.readline(3).format(sale.document))
                pdf.drawString(30, h-310, companyContract.readline(15))
                pdf.drawString(30, h-330, companyContract.readline(3).format(sale.address))
                pdf.setFont('Helvetica-Bold', 14)
                pdf.drawString(30, h-350, 'OBJETO DEL CONTRATO')
                pdf.setFont('Helvetica', 14)

            pdf.showPage()
            pdf.save()

            return response

        else:

            context = area(request, response = form.errors)

            return render(request, 'Finanzas_sales.html', context= context)

    return render(request, 'Finanzas_sales.html', context= context)

@login_required(login_url='index')
def todaysAbstract(request):

    abstract = Sales.objects.filter(date__day=timezone.datetime.today().day)

    context = area(request, abstract=abstract)

    return render(request, 'Finanzas_todaysAbstract.html', context=context)