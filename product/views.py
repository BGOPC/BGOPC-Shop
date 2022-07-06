from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import *
# from django.db.models import Q
from django.http import HttpResponseRedirect
# from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.
def products(request):
    all_products = Product.objects.all()

    return render(request, 'product/products.html', {
        'products': all_products.order_by("title"),
        'pcount': all_products.count(),
        'price': all_products.aggregate(Avg("price"), Min("price"), Max("price")),
    })


def products_red(request):
    url = reverse('products')
    return HttpResponseRedirect(url)


def product(request, ps):
    single_product = get_object_or_404(Product, slug=ps)
    return render(request, "product/product.html", {
        'product': single_product
    })


def contact(request):
    return render(request, 'product/Contact.html')

def site_header_partial(request):
    return render(request, 'shared/site_header.html', )