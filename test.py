from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4

pdf = canvas.Canvas('reports/report{num}.pdf'.format(num= 1), pagesize =A4)
pdf.setFont('Times-Roman', 15)
pdf.drawString((w/2)-50, h-20, 'Documento N°: {num}'.format(num= 1))
pdf.drawString(10, h-50, 'Vendedor: {vendor}'.format(vendor= 'Juan Paliza'))
pdf.drawString(10, h-80, 'Nombre: {name}'.format(name= 'Ramiro Chavez'))
pdf.drawString(10, h-110, 'Direccion: {address}'.format(address= 'Urb. La cultura A-2'))
pdf.drawString(10, h-140, 'Distrito: {district}'.format(district= 'Cusco'))
pdf.drawString(10, h-170, 'Referencia: {refference}'.format(refference= 'Cerca a Mariscal Gamarra'))
pdf.drawString(10, h-200, 'Telefono: {phone}'.format(phone= 'Cerca a Mariscal Gamarra'))
pdf.drawString(10, h-230, 'E-mail: {mail}'.format(mail= 'test@gmail.com'))
pdf.drawString(10, h-260, 'Obaservaciones: {observations}'.format(observations= 'No hay observaciones'))
pdf.drawString(10, h-290, 'Prioridad: {priority}'.format(priority= 'A'))
pdf.drawString(10, h-320, 'Servicio: {service}'.format(service= 'Ambos'))
pdf.drawString(10, h-350, 'Fecha: {date}'.format(date= '2021-03-03'))
pdf.drawString(10, h-380, 'Fecha de instalacion: {install_date}'.format(install_date= '2021-10-12'))
pdf.drawString(10, h-410, 'Materiales: {materials}'.format(materials= '250 metros de cable'))
pdf.drawString(10, h-440, 'Precio: {price}'.format(price= 50))
pdf.drawString((w/2)-50, h-480, '...............................')
pdf.drawString((w/2)-10, h-500, 'Firma')
pdf.showPage()
pdf.save()