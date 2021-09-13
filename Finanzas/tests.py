# Django modules
from django.test import TestCase
from django.utils import timezone

# Own modules
from Finanzas.models.SalesFormModels import Sales


class FinanazasTest(TestCase):

    def setUp(self) -> None:
        
        self.sales = Sales.objects.create(
        document = 2072948331,
        speed = "200mb",
        province = "Cusco",
        payment = 'El 10 de cada mes',
        ip = '200', 
        vendor = 'r13_96@gmail.com', 
        name = 'Sebastian', 
        address = 'Av. La cultura', 
        district = 'Wanchaq',
        refference = 'Parque San Borja', 
        phone = '984338833/95048395', 
        mail = 'ym@gmail.com', 
        observations = 'Sin observaciones', 
        priority = 'A', 
        service = 'Ambos', 
        install_date = '2021-05-11', 
        materials = '200 metros de cable',
        toPay = '2000',
        status = 'Cancelacion',
        price = 0
        )
    
    def test_sales(self) -> None:

        self.assertEqual(self.sales.document, 2072948331)
        self.assertEqual(self.sales.speed, '200mb')
        self.assertEqual(self.sales.province, 'Cusco')
        self.assertEqual(self.sales.payment, 'El 10 de cada mes')
        self.assertEqual(self.sales.ip, '200')
        self.assertEqual(self.sales.company, False)
        self.assertEqual(self.sales.vendor, 'r13_96@gmail.com')
        self.assertEqual(self.sales.name, 'Sebastian')
        self.assertEqual(self.sales.address, 'Av. La cultura')
        self.assertEqual(self.sales.district, 'Wanchaq')
        self.assertEqual(self.sales.refference, 'Parque San Borja')
        self.assertEqual(self.sales.phone, '984338833/95048395')
        self.assertEqual(self.sales.mail, 'ym@gmail.com')
        self.assertEqual(self.sales.observations, 'Sin observaciones')
        self.assertEqual(self.sales.priority, 'A')
        self.assertEqual(self.sales.service, 'Ambos')
        self.assertEqual(self.sales.date, timezone.now().date())
        self.assertEqual(self.sales.install_date, '2021-05-11')
        self.assertEqual(self.sales.materials, '200 metros de cable')
        self.assertEqual(self.sales.toPay, '2000')
        self.assertEqual(self.sales.status, 'Cancelacion')
        self.assertEqual(self.sales.price, 0)