from django.shortcuts import render, redirect
from .models import *
from .database import Session


def order_create(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        with Session() as session:
            order = Order(person_name=person_name)
            session.add(order)
            session.flush()
            order_product = OrderProduct(order_id=order.id, product_id=product_id, quantity=quantity)
            session.add(order_product)
            session.commit()

        return redirect('order_list')

    products = Session().query(Product).all()
    return render(request, 'orders/order_form.html', {'products': products})


def order_list(request):
    with Session() as session:
        orders = session.query(Order).all()
        orders_info = []
        for order in orders:
            total_cooking_time = sum(
                op.quantity * session.query(Product).filter_by(id=op.product_id).first().time_to_cook for op in
                order.products)
            orders_info.append((order, total_cooking_time))
    return render(request, 'orders/order_list.html', {'orders_info': orders_info})