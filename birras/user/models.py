from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    # aca se podra manipulara los objetos usuario

    def create_user(self, email, password, name=None, last_name=None):
        #Crear nuevo User
        if not email:
            raise ValueError('Debe ingresar un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        #crea un administrador.
        user = self.create_user(email, password)

        #indicamos que es un administrador
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    
    # va a ser unico por usuario
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)


    # se activa al momento de crar el usuario
    is_active = models.BooleanField(default=True)

    # no va a ser admin hasta que el superuser lo indique
    is_staff = models.BooleanField(default=False)

    # permite manipular los datos del usuario
    objects = UserManager()

    # campos con los que se va a loguear el usuario
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELD = ['name']

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.name
