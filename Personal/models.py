#django modules

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

AREAS = (
    ('Gerencia geneal', 'Gerencia'),
    ('RRHH', 'Recursos humanos'),
    ('Ventas', 'Ventas'),
)

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, last_name, start_date, salary, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        area = AREAS[0][0]

        return self.create_user(email, user_name, last_name, start_date, area, salary, password, **other_fields)

    def create_user(self, email, user_name, last_name, start_date, area, salary, password, **other_fields):

        if not email:
            raise ValueError(_('Debes proveer una direccion de e-mail'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          last_name=last_name, start_date=start_date, area=area, salary=salary,**other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('E-mail'), unique=True)
    user_name = models.CharField(_('Nombres del usuario'), max_length=150)
    last_name = models.CharField(_('Apellidos del usuario'), max_length=150)
    start_date = models.DateField(_('Fecha de inicio'))
    area = models.CharField(_('Area de trabajo'), max_length=100, choices=AREAS)
    position = models.CharField(_('Puesto dentro del area'), max_length=200)
    salary = models.FloatField(_('Salario'))
    is_staff = models.BooleanField(_('Es staff'), default=False)
    is_active = models.BooleanField(_('Es activo'), default=False)
    is_superuser = models.BooleanField(_('Es superusuario'), default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'last_name', 'start_date', 'salary']

    def __str__(self):
        return self.email

    class Meta:

        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'