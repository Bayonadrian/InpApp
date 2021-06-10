#django modules
from django.urls import path
#own modules
from Personal.views import index, exit

urlpatterns = [
    path('', index, name='index'),
    path('exit', exit, name='exit'),
]