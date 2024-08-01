import os
import django
from django.db.models import Q, Count, F, Case, When, Value, BooleanField

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
# Import your models here
from main_app.models import Profile, Product, Order


# Create queries within functions
def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    query = (
            Q(full_name__icontains=search_string) |
            Q(email__icontains=search_string) |
            Q(phone_number__icontains=search_string)
    )
    profiles = Profile.objects.filter(query).order_by('full_name')

    if not profiles:
        return ""

    return '\n'.join(
        f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_profile.count()}"
        for p in profiles)


def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.orders_count}" for p in profiles)


def get_last_sold_products() -> str:
    order = Order.objects.prefetch_related('products').last()

    if not order or not order.products:
        return ""

    products = ', '.join(order.products.values_list('name', flat=True).order_by('name'))

    return f"Last sold products: {products}"


def get_top_products() -> str:
    products = Product.objects.annotate(
        product_count=Count('orders_products')
    ).filter(product_count__gt=0).order_by('-product_count', 'name')[:5]

    if not products:
        return ""

    return f"Top products:\n" + '\n'.join(f"{p.name}, sold {p.product_count} times" for p in products)


def apply_discounts() -> str:
    orders = Order.objects.filter(is_completed=False, products__gt=2).update(total_price=F('total_price') * 0.9)

    # return f"Discount applied to {orders if orders else 0} orders."
    return f"Discount applied to {orders} orders."


def complete_order() -> str:
    order = Order.objects.filter(is_completed=False).first()
    if not order:
        return ""

    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),
            default=F('is_available'),
            output_field=BooleanField()
    ))

    order.is_completed = True
    order.save()

    return "Order has been completed!"
