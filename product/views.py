from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product
# from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import Http404


# Create your views here.
def products(request):
    all_products = Product.objects.all()

    return render(request, 'product/products.html', {
        'products': all_products,
    })


def products_red(request):
    url = reverse('products')
    return HttpResponseRedirect(url)


def product(request, pid):
    # try:
        # single_product = Product.objects.get(id=pid)
    # except:
        # raise Http404()
    single_product = get_object_or_404(Product, pk=pid)
    return render(request, "product/product.html", {
        'product': single_product,
    })
