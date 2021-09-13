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

STATUS = (
    ('Activo', 'Activo'),
    ('Temporal', 'Corte temporal'),
    ('Mora', 'Corte por mora'),
    ('Cancelacion', 'Corte por cancelacion del contrato'),
)

class Sales(models.Model):

    document = models.IntegerField(verbose_name='Dni/Ruc', unique=True)
    company = models.BooleanField(verbose_name='Es una empresa', default=False)
    speed = models.CharField(verbose_name="Velocidad de internet", max_length=20)
    province = models.CharField(verbose_name="Provincia a la que pertenece", max_length=50)
    payment = models.CharField(verbose_name='Fecha de pago', max_length=100)
    ip = models.CharField(verbose_name='Cantidad de ip', max_length=300)
    vendor = models.CharField(verbose_name='Vendedor', max_length=150)
    name = models.CharField(verbose_name='Nombre del cliente', max_length=200)
    address = models.CharField(verbose_name='Direccion', max_length=200)
    district = models.CharField(verbose_name='Distrito', max_length=100)
    refference = models.CharField(verbose_name='Referencia', max_length=150, blank=True)
    phone = models.CharField(verbose_name='Telefono', max_length=200)
    mail = models.CharField(verbose_name='Correo electronico', max_length=150, blank=True)
    observations = models.TextField(verbose_name='Observaciones', blank=True)
    priority = models.CharField(verbose_name='Prioridad', max_length=1, choices=PRIORITIES)
    service = models.CharField(verbose_name='Servicios', max_length=10, choices=SERVICES)
    date = models.DateField(verbose_name='Fecha', auto_now_add=True)
    install_date = models.DateField(verbose_name='Fecha de instalacion', blank=True, null=True)
    materials = models.TextField(verbose_name='Materiales', blank=True)
    status = models.CharField(verbose_name='Status del servicio', max_length=20, choices=STATUS, blank=True)
    price = models.FloatField(verbose_name='Precio')

    def __str__(self) -> str:
        return str(self.document)

    class Meta:

        verbose_name = 'Formulario de venta'
        verbose_name_plural = 'Formularios de ventas'