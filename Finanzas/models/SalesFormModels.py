from django.db import models

PRIORITIES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
)

SERVICES = (
    ('Tv', 'Tv'),
    ('Internet', 'Internet'),
    ('Ambos', 'Ambos'),
)

class Sales(models.Model):

    document = models.IntegerField(verbose_name='Dni/Ruc')
    company = models.BooleanField(verbose_name='Es una empresa', default=True)
    vendor = models.CharField(verbose_name='Vendedor', max_length=150)
    name = models.CharField(verbose_name='Nombre del cliente', max_length=200)
    address = models.CharField(verbose_name='Direccion', max_length=200)
    district = models.CharField(verbose_name='Distrito', max_length=100)
    refference = models.CharField(verbose_name='Referencia', max_length=150)
    phone = models.IntegerField(verbose_name='Telefono')
    mail = models.CharField(verbose_name='Correo electronico', max_length=150)
    observations = models.TextField(verbose_name='Observaciones', blank=True)
    priority = models.CharField(verbose_name='Prioridad', max_length=1, choices=PRIORITIES)
    service = models.CharField(verbose_name='Servicios', max_length=10, choices=SERVICES)
    date = models.DateField(verbose_name='Fecha', auto_now_add=True)
    install_date = models.DateField(verbose_name='Fecha de instalacion')
    materials = models.TextField(verbose_name='Materiales')
    price = models.FloatField(verbose_name='Precio')

    class Meta:

        verbose_name = 'Formulario de venta'
        verbose_name_plural = 'Formularios de ventas'