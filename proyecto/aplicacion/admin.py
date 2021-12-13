from django.contrib import admin
from .models import Cliente, Habitacion, Ocupacion
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Ocupacion)
