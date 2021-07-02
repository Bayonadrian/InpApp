#django modules
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#python modules
import io
#third party-modules
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
#own modules
from Personal.functions import area
from Finanzas.forms import SalesForm, Sales


@login_required(login_url='index')
def sales(request):

    form = SalesForm()

    context = area(request)

    if request.method == 'POST':

        data = {
            'document': request.POST['document'],
            'company': request.POST['company'],
            'vendor': request.user,
            'name': request.POST['name'],
            'address': request.POST['address'],
            'district': request.POST['district'],
            'refference': request.POST['refference'],
            'speed': request.POST['speed'],
            'province': request.POST['province'],
            'payment': request.POST['payment'],
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
            pdf.setFont('Times-Roman', 15)
            pdf.drawString((w/2)-50, h-20, 'Documento N°: {num}'.format(num= sale.id))
            pdf.drawString(10, h-50, 'Vendedor: {vendor}'.format(vendor= sale.vendor))
            pdf.drawString(10, h-80, 'Nombre: {name}'.format(name= sale.name))
            pdf.drawString(10, h-110, 'Direccion: {address}'.format(address= sale.address))
            pdf.drawString(10, h-140, 'Distrito: {district}'.format(district= sale.district))
            pdf.drawString(10, h-170, 'Referencia: {refference}'.format(refference= sale.refference))
            pdf.drawString(10, h-200, 'Velocidad de internet: {speed}'.format(speed= sale.speed))
            pdf.drawString(10, h-230, 'Province: {province}'.format(province= sale.province))
            pdf.drawString(10, h-260, 'Fecha de inicio y pagos: {payment}'.format(payment= sale.payment))
            pdf.drawString(10, h-290, 'Telefono: {phone}'.format(phone= sale.phone))
            pdf.drawString(10, h-320, 'E-mail: {mail}'.format(mail= sale.mail))
            pdf.drawString(10, h-350, 'Obaservaciones: {observations}'.format(observations= sale.observations))
            pdf.drawString(10, h-380, 'Prioridad: {priority}'.format(priority= sale.priority))
            pdf.drawString(10, h-410, 'Servicio: {service}'.format(service= sale.service))
            pdf.drawString(10, h-440, 'Fecha: {date}'.format(date= sale.date))
            pdf.drawString(10, h-470, 'Precio: {price}'.format(price= sale.price))
            pdf.drawString((w/2)-50, h-500, '...............................')
            pdf.drawString((w/2)-10, h-530, 'Firma')
            pdf.showPage()
            pdf.save()

            return response

        else:

            context = area(request, response = form.errors)

            return render(request, 'Finanzas_sales.html', context= context)

    return render(request, 'Finanzas_sales.html', context= context)