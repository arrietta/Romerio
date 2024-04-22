import json
import uuid

from django.http import JsonResponse

from Main.models import *
from django.shortcuts import render, redirect


def identification(request):
    unique_id = request.session.get('unique_id', 'Not available')
    if not unique_id or unique_id == 'Not available':
        unique_id = str(uuid.uuid4())
        request.session['unique_id'] = unique_id
    else:
        unique_id = request.session.get('unique_id', 'Not available')
    return unique_id


def main(request):
    unique_id = identification(request)
    return render(request, 'main.html')


def catalog(request):
    return render(request, 'catalog.html')


def cart(request):
    unique_id = identification(request)
    return render(request, 'cart.html')


def constructor(request, key):

    if 'shpon' in key:
        print("spon")
    collections = Collections.objects.get(name=key)
    shape = Shape.objects.filter(collections=collections.pk)
    portal = Portal.objects.all()
    carnice = Carnice.objects.all()
    podium = Podium.objects.all()
    socket = Socket.objects.all()
    boots = Boots.objects.all()
    molding = Molding.objects.filter(collections=collections.pk)

    return render(request, 'Constructor.html',
                  {'shape_data': Data(shape),
                   'portal_data': Data(portal),
                   'molding_data': Data(molding),
                   'podium_data': Data(podium),
                   'boots_data': Data(boots),
                   'carnice_data': Data(carnice),
                   'socket_data': Data(socket)})


def Data(data):
    return json.dumps(list(data.values()))


def api(request):
    unique_id = identification(request)
    if request.method == 'POST':

        cart_item = CartItem.objects.create(
            Key=unique_id,
            image=request.POST['image'],
            bevel=request.POST['bevel'],
            shape=request.POST['shape'],
            molding=request.POST['molding'],
            portal=request.POST['portal'],
            carnice=request.POST['carnice'],
            podium=request.POST['podium'],
            socket=request.POST['socket'],
            boots=request.POST['boots'],
            door_price=request.POST['price'],
            size=request.POST['size'],
            quantity=1
        )
        cart_item.save()

        return redirect("/cart/")
