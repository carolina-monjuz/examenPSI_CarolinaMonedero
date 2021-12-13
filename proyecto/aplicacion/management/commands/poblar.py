import os

from django.core.management.base import BaseCommand
from aplicacion.models import (Cliente, Habitacion, Ocupacion)
# from faker import Faker
# from decimal import Decimal
# # define STATIC_PATH in settings.py
# from bookshop.settings import STATIC_PATH
# from PIL import Image, ImageDraw, ImageFont
# from django.utils.timezone import make_aware


FONTDIR = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#

# faker = Faker()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.cliente()
        self.habitacion()
        self.ocupacion()

    def cleanDataBase(self):
        Cliente.objects.all().delete()
        Habitacion.objects.all().delete()
        Ocupacion.objects.all().delete()

    def cliente(self):

        clientes = [
            {
                'id': 1001,
                'nombreCliente': 'Frodo Bolsón',
                'fechaAlta': '2019-04-08'
            },
            {
                'id': 1002,
                'nombreCliente': 'Samsagaz Gamyi',
                'fechaAlta': '2020-07-14'
            },
            {
                'id': 1003,
                'nombreCliente': 'Peregrin Tuk',
                'fechaAlta': '2021-03-08'
            }
        ]

        for u in clientes:
            u = Cliente(id=u['id'], nombreCliente=u['nombreCliente'], fechaAlta=u['fechaAlta'])
            u.save()

    def habitacion(self):

        habitaciones = [
            {
                'id': 1001,
                'numeroCamas': 2,
                'situacion': 'vistas a Mordor',
            },
            {
                'id': 1002,
                'numeroCamas': 1,
                'situacion': 'vistas a Belagaer',
            },
            {
                'id': 1003,
                'numeroCamas': 3,
                'situacion': 'vistas a la Comarca',
            }
        ]

        for t in habitaciones:
            t = Habitacion(id=t['id'], numeroCamas=t['numeroCamas'], situacion=t['situacion'])
            t.save()

    def ocupacion(self):

        ocups = [
            {
                'id': 1001,
                'cliente': Cliente.objects.get(id=1001),
                'habitacion': Habitacion.objects.get(id=1001),
                'fechaEntrada': '2021-03-21',
                'fechaSalida': '2021-03-22'
            },
            {
                'id': 1002,
                'cliente': Cliente.objects.get(id=1002),
                'habitacion': Habitacion.objects.get(id=1001),
                'fechaEntrada': '2021-07-21',
                'fechaSalida': '2021-07-24'
            },
            {
                'id': 1003,
                'cliente': Cliente.objects.get(id=1003),
                'habitacion': Habitacion.objects.get(id=1002),
                'fechaEntrada': '2021-05-25',
                'fechaSalida': '2021-05-31'
            },
            {
                'id': 1004,
                'cliente': Cliente.objects.get(id=1002),
                'habitacion': Habitacion.objects.get(id=1003),
                'fechaEntrada': '2021-08-22',
                'fechaSalida': '2021-08-25'
            }
        ]

        for r in ocups:
            r = Ocupacion(id=r['id'], cliente=r['cliente'], habitacion=r['habitacion'], fechaEntrada=r['fechaEntrada'], fechaSalida=r['fechaSalida'])
            r.save()