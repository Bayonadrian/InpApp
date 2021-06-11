#django modules
from django.forms import ModelForm
#own modules
from Finanzas.models.SalesFormModels import Sales

class SalesForm(ModelForm):

    class Meta:

        model = Sales
        fields = '__all__'