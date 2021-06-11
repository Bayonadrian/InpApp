#django modules
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
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

            buffer = io.BytesIO()

            pdf = canvas.Canvas(buffer, pagesize =A4)
            pdf.setFont('Times-Roman', 15)
            pdf.drawString((w/2)-50, h-20, 'Documento N°: {num}'.format(num= sale.id))
            pdf.drawString(10, h-50, 'Vendedor: {vendor}'.format(vendor= sale.vendor))
            pdf.drawString(10, h-80, 'Nombre: {name}'.format(name= sale.name))
            pdf.drawString(10, h-110, 'Direccion: {address}'.format(address= sale.address))
            pdf.drawString(10, h-140, 'Distrito: {district}'.format(district= sale.district))
            pdf.drawString(10, h-170, 'Referencia: {refference}'.format(refference= sale.refference))
            pdf.drawString(10, h-200, 'Telefono: {phone}'.format(phone= sale.phone))
            pdf.drawString(10, h-230, 'E-mail: {mail}'.format(mail= sale.mail))
            pdf.drawString(10, h-260, 'Obaservaciones: {observations}'.format(observations= sale.observations))
            pdf.drawString(10, h-290, 'Prioridad: {priority}'.format(priority= sale.priority))
            pdf.drawString(10, h-320, 'Servicio: {service}'.format(service= sale.service))
            pdf.drawString(10, h-350, 'Fecha: {date}'.format(date= sale.date))
            pdf.drawString(10, h-380, 'Fecha de instalacion: {install_date}'.format(install_date= sale.install_date))
            pdf.drawString(10, h-410, 'Materiales: {materials}'.format(materials= sale.materials))
            pdf.drawString(10, h-440, 'Precio: {price}'.format(price= sale.price))
            pdf.drawString((w/2)-50, h-480, '...............................')
            pdf.drawString((w/2)-10, h-500, 'Firma')
            pdf.showPage()
            pdf.save()

            buffer.seek(0)

            return FileResponse(buffer, as_attachment=True, filename= 'report{num}.pdf'.format(num= sale.id))

        else:

            context = area(request, response = form.errors)

            return render(request, 'Finanzas_sales.html', context= context)

    return render(request, 'Finanzas_sales.html', context= context)