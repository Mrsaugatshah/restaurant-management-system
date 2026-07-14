from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Order, OrderHistory


@receiver(pre_save, sender=Order)
def handle_order_pre_save(sender, instance, **kwargs):

    if instance.pk:
        old_order = Order.objects.get(pk=instance.pk)
        instance._old_status = old_order.status
    else:
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