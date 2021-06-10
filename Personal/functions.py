#own modules
from django.contrib.auth import get_user_model

def area(request, **kwargs):

    user = get_user_model()

    area = user.objects.get(email= request.user)

    kwargs['area'] = area.area

    return kwargs
