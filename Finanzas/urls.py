#django modules
from django.urls import path
#own modules
from Finanzas.views import sales, todaysAbstract

urlpatterns = [
    path('sales/', sales, name='Finanzas_sales'),
    path('todaysAbstract/', todaysAbstract, name='Finanzas_todaysAbstract'),
]