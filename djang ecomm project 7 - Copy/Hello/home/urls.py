# from django.contrib import admin
# from django.urls import path
# from home import views


# urlpatterns = [
#     path("", views.store, name='store'),
#     path("checkout/", views.checkout, name='checkout'),
#     path("cart/", views.cart, name='cart'),

#     path("update_item/", views.updateItem, name='update_item'),
#     path("continue_view/", views.continue_view, name='continue_view'),
    
# ]
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.store, name='store'),
    path("checkout/", views.checkout, name='checkout'),
    path("cart/", views.cart, name='cart'),
    path("update_item/", views.updateItem, name='update_item'),
    path("continue_view/", views.continue_view, name='continue_view'),
]
