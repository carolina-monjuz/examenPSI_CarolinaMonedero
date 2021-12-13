from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('cliente/<int:pk>/', views.cliente_detail, name='cliente'),

]

