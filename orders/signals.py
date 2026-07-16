from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Order, OrderHistory,OrderItem



@receiver(pre_save, sender=Order)
def handle_order_pre_save(sender, instance, **kwargs):

    try:
        old_order = Order.objects.get(pk=instance.pk)
        instance._old_status = old_order.status
    except Order.DoesNotExist:
        instance._old_status = None



@receiver(post_save, sender=Order)
def handle_order_history_creation(sender, instance, created, **kwargs):

    # New order created
    if created:
        OrderHistory.objects.create(
            order=instance,
            status=instance.status
        )
        return


    # Existing order status changed
    if hasattr(instance, "_old_status"):

        if instance._old_status != instance.status:

            OrderHistory.objects.create(
                order=instance,
                status=instance.status
            )

            print("Previous status:", instance._old_status)
            print("New status:", instance.status)
            
            
@receiver(post_save, sender=OrderItem)
def handle_auto_order_status_update(sender, instance, **kwargs):

    order = instance.order

    if order is None:
        return

    items = order.order_items.all()

    if all(item.status == OrderItem.ITEM_STATUS.SERVED for item in items):
        order.status = Order.ORDER_STATUS.SERVED
    else:
        order.status = Order.ORDER_STATUS.PARTIALLY_SERVED

    order.save()

    print("Order status updated to:", order.status)
        