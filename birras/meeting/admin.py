from django.contrib import admin
from .models import Meeting

# Register your models here.


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'invitados','fecha_hora', 'temp_max', 'cajas_birra',)
    
    readonly_fields = ('created', 'updated', 'cajas_birra', 'temp_max')

admin.site.register(Meeting, MeetingAdmin)
