from django.http import JsonResponse

from Main.models import *
from django.shortcuts import render, redirect
import json
import uuid

from Main.telegram_bot import send_photo_with_message_to_bot


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
    if request.method == 'POST':
        Name = "Конечный заказчик: " + request.POST['name'] + '\n'
        phone = "Контактный телефон: " + request.POST['phone'] + '\n'
        delivery = "Доставка: " + ("Есть" if request.POST['delivery'] else "") + '\n'
        sizeing = "Замеры: " + ("Есть" if request.POST['measurement'] else "") + '\n'

        id = identification(request)

        with open('data.json', 'r', encoding='utf-8') as file:
            # Load JSON data
            data = json.load(file)

        Doors = CartItem.objects.filter(Key=id)
        for i in Doors:
            shape = "- Форма: " + (i.shape.split("_")[0] + " " + data[i.shape.split("_")[1]] if i.shape.split("_")[
                                                                                                    1] in data else i.shape) + "\n"
            portal = "- Портал: " + (data[i.portal] if i.portal in data else i.portal) + "\n"
            color = "- Цвет: " + (data[i.color] if i.color in data else i.color) + "\n"
            image = i.image
            price = "- Цена: " + str(i.door_price * i.quantity) + "\n"
            quantity = "- Количество: " + str(i.quantity) + "\n"

            bevel = "- Фреза: " + (data[i.bevel] if i.bevel in data else i.bevel) + "\n" if i.bevel != "null" else ""
            grid = "- Решётка: " + (data[i.grid] if i.grid in data else i.grid) + "\n" if i.grid != "null" else ""
            grid_bevel = "- Фреза Решётки: " + (
                data[i.grid_bevel] if i.grid_bevel in data else i.grid_bevel) + "\n" if i.grid_bevel != "null" else ""
            molding = "- Багет/Вставка: " + (
                data[i.molding] if i.molding in data else i.molding) + "\n" if i.molding != "null" else ""
            carnice = "- Карниз: " + (
                data[i.carnice] if i.carnice in data else i.carnice) + "\n" if i.carnice != "null" else ""
            podium = "- Возвышение: " + (
                data[i.podium] if i.podium in data else i.podium) + "\n" if i.podium != "null" else ""
            socket = "- Розетка: " + (
                data[i.socket] if i.socket in data else i.socket) + "\n" if i.socket != "null" else ""
            boots = "- Сапожок: " + (data[i.boots] if i.boots in data else i.boots) + "\n" if i.boots != "null" else ""

            massage = (Name + phone + delivery + sizeing + shape + grid + grid_bevel + color +
                       bevel + molding + portal + carnice +
                       podium + socket + boots + price + quantity)

            send_photo_with_message_to_bot(image, massage)

            # send_message_to_bot(massage)
            i.delete()
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
            icon=request.POST['icon'],
            bevel=request.POST['bevel'],
            grid=request.POST['grid'],
            grid_bevel=request.POST['grid_bevel'],
            shape=request.POST['shape'],
            molding=request.POST['molding'],
            portal=request.POST['portal'],
            carnice=request.POST['carnice'],
            podium=request.POST['podium'],
            socket=request.POST['socket'],
            boots=request.POST['boots'],
            door_price=request.POST['price'],
            size=request.POST['size'],
            color=request.POST['color_name'],
            quantity=1
        )
        print(request.POST['price'])
        cart_item.save()

        return redirect("/Cart/")


def api_plus(request):
    if request.method == 'POST':
        key = request.POST.get("key")
        item_id = request.POST.get("id")

        if key and item_id:
            cart_item = CartItem.objects.get(Key=key, id=item_id)
            cart_item.quantity += 1
            cart_item.save()

            if cart_item:
                return JsonResponse({'success': True, 'message': 'CartItem found.'})
            else:
                return JsonResponse({'success': False, 'message': 'CartItem not found.'})
        else:
            return JsonResponse({'success': False, 'message': 'Key and/or id parameter missing.'})

    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are supported.'})


def api_minus(request):
    if request.method == 'POST':
        key = request.POST.get("key")
        item_id = request.POST.get("id")

        if key and item_id:
            cart_item = CartItem.objects.get(Key=key, id=item_id)
            cart_item.quantity -= 1
            cart_item.save()

            if cart_item:
                return JsonResponse({'success': True, 'message': 'CartItem found.'})
            else:
                return JsonResponse({'success': False, 'message': 'CartItem not found.'})
        else:
            return JsonResponse({'success': False, 'message': 'Key and/or id parameter missing.'})

    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are supported.'})


def api_delete(request):
    if request.method == 'POST':
        key = request.POST.get("key")
        item_id = request.POST.get("id")

        if key and item_id:
            cart_item = CartItem.objects.get(Key=key, id=item_id)
            cart_item.delete()

            if cart_item:
                return JsonResponse({'success': True, 'message': 'CartItem found.'})

            else:
                return JsonResponse({'success': False, 'message': 'CartItem not found.'})
        else:
            return JsonResponse({'success': False, 'message': 'Key and/or id parameter missing.'})

    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are supported.'})


def Shpon(request, key):
    collections = Collections.objects.get(name=key)
    shape = Shpone.objects.filter(collections=collections.pk)
    carnice = Shpon_Carnice.objects.all()
    socket = Shpon_Socket.objects.all()
    boots = Shpon_Boots.objects.all()
    molding = Shpon_Molding.objects.filter(collections=collections.pk)

    return render(request, 'Shpon.html',
                  {'shape_data': Dump(shape),
                   'molding_data': Dump(molding),
                   'boots_data': Dump(boots),
                   'carnice_data': Dump(carnice),
                   'socket_data': Dump(socket)})


def privacy(request):
    return render(request, 'privacy.html')
