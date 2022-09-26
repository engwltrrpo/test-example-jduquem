from datetime import datetime
from django.shortcuts import render, redirect
from .models import vehiculo
from django.http import JsonResponse

def home(request):
    return render(request, 'blank.html')

def vehiculos(request):
    queryset = vehiculo.objects.all()
    return render(request, 'gestionvehiculo.html', {'queryset':queryset})

def registrarvehiculo(request):
    placa=request.POST['txtplaca']
    capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
    cilindraje=request.POST['numcilindraje']
    fecha_SOAT=request.POST['numfecha_SOAT']
    tarjeta_operacion=request.POST['numtarjeta_operacion']
    propietario=request.POST['numpropietario']
    estado=request.POST['numestado']

    vehiculo.objects.create(placa = placa, capacidad_de_pasajeros=capacidad_de_pasajeros, cilindraje=cilindraje, tarjeta_operacion=tarjeta_operacion, fecha_SOAT=fecha_SOAT, propietario=propietario, estado=estado)
    return redirect('vehiculos')

def edicionvehiculo(request, placa):
    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.fecha_SOAT = datetime.strptime(str(vehiculos.fecha_SOAT), '%Y-%m-%d').strftime('%Y-%m-%d')
    vehiculos.tarjeta_operacion = datetime.strptime(str(vehiculos.tarjeta_operacion), '%Y-%m-%d').strftime('%Y-%m-%d')
    return render(request, 'edicionvehiculo.html', {'vehiculo': vehiculos})

def editarvehiculo(request):
    placa=request.POST['txtplaca']
    capacidad_de_pasajeros=request.POST['txtcapacidad_de_pasajeros']
    cilindraje=request.POST['numcilindraje']
    fecha_SOAT=request.POST['numfecha_SOAT']
    tarjeta_operacion=request.POST['numtarjeta_operacion']
    propietario=request.POST['numpropietario']
    estado=request.POST['numestado']

    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.capacidad_de_pasajeros = capacidad_de_pasajeros
    vehiculos.cilindraje= cilindraje
    vehiculos.fecha_SOAT= fecha_SOAT
    vehiculos.tarjeta_operacion=tarjeta_operacion
    vehiculos.propietario= propietario
    vehiculos.estado = estado
    vehiculos.save()
    return redirect('vehiculos')

def eliminarvehiculo(request, placa):
    vehiculos = vehiculo.objects.get(placa=placa)
    vehiculos.delete()
    return redirect('vehiculos')


def jgetVehiculo(request, pk):
    from djongo import models
    try:
        Vehiculos = vehiculo.objects.get(pk=ObjectId(pk))
    except vehiculo.DoesNotExist:
        return JsonResponse('')
    
    return JsonResponse({
        'placa': Vehiculos.placa,
        'capacidad_de_pasajeros': Vehiculos.capacidad_de_pasajeros,
        'cilindraje': Vehiculos.cilindraje,
        'fecha_SOAT': Vehiculos.fecha_SOAT,
        'propietario': Vehiculos.propietario,
        'estado':Vehiculos.estado
    })