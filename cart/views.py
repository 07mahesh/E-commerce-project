from django.shortcuts import render,redirect
from store.models import product
from cart.models import Cart,CartItem



# def _cart_id(request):
#     cart=request.session.session_key
#     if not cart:
#         cart= request.session.create()
#     return cart


# def add_cart(request,product_id):
#     product_cart=product.objects.get(id=product_id) 
#     try:
#         cart=Cart.objects.get(cart_id=_cart_id(request))
#     except Cart.DoesNotExist:
#         cart=Cart.objects.create(
#             cart_id=_cart_id(request)
#         )
#         cart.save()

#         try:
#             cart_item=CartItem.objects.get(product_cart=product,cart=Cart)
#             cart_item.quantity+=1
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item=CartItem.objects.create(
#                 product_cart=product,
#                 quantity=1,
#                 cart=Cart
#             )
#             cart_item.save()
#         return redirect('cart') 

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product_cart = product.objects.get(id=product_id)  # Correct field
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
    
    try:
        cart_item = CartItem.objects.get(product=product_cart, cart=cart)  # Use 'product'
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product_cart,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    
    return redirect('cart')






def remove_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))
    product_cart = product.objects.get(id=product_id)  # Fetch the product
    cart_item = CartItem.objects.get(product=product_cart, cart=cart)  # Use 'product'
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')








def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity  # Use 'product'
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        cart_items = []
        total = 0
        quantity = 0

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'store/cart.html', context)

