from django.urls import path

from .views import buy_item, buy_order, item_detail, orders

urlpatterns = [
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),

    # Дополнительное задание
    path('orders/', orders, name='orders'),
    path('payment/<int:order_id>/', buy_order, name='order')
]