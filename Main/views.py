from Main.models import *
from django.shortcuts import render, redirect
import json
import uuid


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
    data = CartItem.objects.filter(Key=unique_id)
    return render(request, 'cart.html', {"data": Dump(data)})


def constructor(request, key):
    collections = Collections.objects.get(name=key)

    shape = Shape.objects.filter(collections=collections.pk)
    portal = Portal.objects.all()
    carnice = Carnice.objects.all()
    podium = Podium.objects.all()
    socket = Socket.objects.all()
    boots = Boots.objects.all()
    molding = Molding.objects.filter(collections=collections.pk)

    return render(request, 'Constructor.html',
                  {'shape_data': Dump(shape),
                   'portal_data': Dump(portal),
                   'molding_data': Dump(molding),
                   'podium_data': Dump(podium),
                   'boots_data': Dump(boots),
                   'carnice_data': Dump(carnice),
                   'socket_data': Dump(socket)})


def Dump(data):
    return json.dumps(list(data.values()))


def api_add(request):
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


def api_plus():
    return None


def api_minus():
    return None