#django modules
from django.urls import path
#own modules
from Finanzas.views import sales

urlpatterns = [
    path('sales/', sales, name='Finanzas_sales'),
]