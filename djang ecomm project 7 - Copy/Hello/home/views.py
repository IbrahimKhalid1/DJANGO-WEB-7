# from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.shortcuts import render, HttpResponse

def store(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']


    products = Product.objects.all()
    context = {'products':products,'cartItems':cartItems}
    return render(request, 'store.html', context)

def continue_view(request):
    # Add data to the context as needed
    context = {
        'key1': 'value1',
        'key2': 'value2',
        # Add more key-value pairs as needed
    }

    # Render the 'continue.html' template with the context
    return render(request, 'continue.html', context)





# Create your views here.
# def store(request):
#     context = {}
#     return render(request, 'store.html' , context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)





def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'checkout.html', context)




# def updateItem(request):
#     data = json.loads(request.data)
#     productId = data['productId']
#     action = data['action']



#     print('Action', action)
#     print('productId', productId)


#     customer = request.user.customer
#     product = Product.object.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)

#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

#     if action == 'add':
#        orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)

#     orderItem.save()

#     if orderItem <= 0:
#        orderItem.delete()



#     return JsonResponse('Item was Added', safe=False)



import json
from django.http import JsonResponse
from .models import Product, Order, OrderItem

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product ID:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse({'message': 'Item was updated successfully'}, safe=False)




    