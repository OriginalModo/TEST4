from celery import shared_task
from .database import Session
from .models import *

@shared_task
def cook_order(order_id):
    with Session() as session:
        order = session.query(Order).filter_by(id=order_id).first()
        if order:
            ...