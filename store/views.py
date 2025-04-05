from django.shortcuts import render,get_object_or_404
from store.models import product
from app1.models import category
from django.http import Http404
from cart.models import Cart,CartItem
from cart.views import _cart_id
from django.http import HttpResponse


def product_all(request, category_slug=None):
    categories=None
    products=None

    if category_slug !=None:
        categories=get_object_or_404(category,slug=category_slug)
        products=product.objects.filter(category = categories, is_avalible=True)
        product_count=products.count()
    else:
        products=product.objects.all()
        product_count=products.count()

    return render(request, 'store/store.html',{'products':products,'product_count':product_count})





def product_detail_page(request, category_slug, product_slug):
    try:
        single_product = product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart= CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
        related_products = single_product.related_products.all()
      
    except product.DoesNotExist:
        raise Http404("Product not found.")
    except Exception as e:
        # Debugging information
        print(f"Error occurred: {e}")
        raise e
    context={
        'single_product': single_product,
        'in_cart':in_cart,
        'related_products': related_products

    }

    return render(request, 'store/product_detail.html', context)







