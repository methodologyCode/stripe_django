import stripe

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum

from Stripe.settings import STRIPE_SECRET_KEY
from .models import Item, Order

stripe.api_key = STRIPE_SECRET_KEY


@csrf_exempt
def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price * 100),
                    # Stripe requires the price in cents
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(f"/success/{item_id}/"),
        cancel_url=request.build_absolute_uri(f"/cancel/{item_id}/"),
    )

    return JsonResponse({"session_id": session.id})


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "item_detail.html", {"item": item})


@csrf_exempt
def buy_order(request, order_id):
    total_sum = (
        Order.objects.filter(pk=order_id)
        .annotate(total_price=Sum("items__price"))
        .values_list("total_price", flat=True)
        .first()
    )

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": f"Заказ номер: {order_id}"},
                    "unit_amount": int(total_sum * 100),
                    # Stripe requires the price in cents
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=request.build_absolute_uri(f"/success/{order_id}/"),
        cancel_url=request.build_absolute_uri(f"/cancel/{order_id}/"),
    )

    return JsonResponse({"session_id": session.id})


def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})
