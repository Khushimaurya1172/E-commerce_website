from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})
def checkout(request):
    if request.method == 'POST':
        # Get dummy data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')

        # Clear cart from session
        request.session['cart'] = {}

        return render(request, 'shop/payment_success.html', {
            'name': name,
            'email': email,
            'address': address
        })

    return render(request, 'shop/checkout.html')
