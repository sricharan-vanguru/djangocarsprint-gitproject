from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars,name='cars'),
    path('<int:id>',views.car_detail,name = 'car_detail'),
    path('search',views.search,name = 'search'),
    path('<int:id>/simple-checkout/',views.simpleCheckout,name = 'simple-checkout'),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete"),
]