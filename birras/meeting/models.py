import requests
import json
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Meeting(models.Model):

    nombre = models.CharField(max_length=50)
    invitados = models.IntegerField()
    imagen = models.ImageField(upload_to='meeting', null= True, blank= True)
    temp_max = models.CharField(max_length=50, null= True)
    cajas_birra = models.IntegerField(null= True)
    fecha_hora = models.DateTimeField()


    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'meeting'
        verbose_name_plural = 'meetings'

    def __str__(self):
        return (self.nombre)

@receiver(post_save, sender= Meeting)
def getCajasBirra(sender, instance, created, **kwargs):
    url = "https://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires&appid=2a160480a24b18d999d7f95410536e1d"
    response = requests.request("GET", url)
    var = json.loads(response.text)
    temp_max = float(var['main']['temp_max'])-273.15
    if temp_max < 20.00:
        cervezas = 0.75
    elif 20.00 <= temp_max <= 24.00:
        cervezas = 1
    else:
        cervezas = 4

    if created:
        cantidad_cervezas = round(float(cervezas) * float(instance.invitados))
        cajas = round(cantidad_cervezas/6)
        instance.temp_max = temp_max
        instance.cajas_birra = cajas
        instance.save()

