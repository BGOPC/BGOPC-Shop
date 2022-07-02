from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product
# from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.
def products(request):
    all_products = Product.objects.all()

    return render(request, 'product/products.html', {
        'products': all_products.order_by("title"),
        'pcount': all_products.count(),
        'avr': all_products.aggregate(Avg("rates")),
        'price': all_products.aggregate(Avg("price"), Min("price"), Max("price")),
    })


def products_red(request):
    url = reverse('products')
    return HttpResponseRedirect(url)


def product(request, ps):
    # try:
        # single_product = Product.objects.get(id=pid)
    # except:
        # raise Http404()
    single_product = get_object_or_404(Product, slug=ps)
    return render(request, "product/product.html", {
        'product': single_product
    })
