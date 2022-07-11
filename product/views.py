# from django.http import Http404
from django.db.models import Avg, Max, Min
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *


# Create your views here.
def home(request):
    all_products = Product.objects.all()

    return render(request, 'product/home.html', {
        'products': all_products.order_by("title"),
        'pcount': all_products.count(),
        'price': all_products.aggregate(Avg("price"), Min("price"), Max("price")),
    })


def products(request):
    all_products = Product.objects.all().order_by("title")[:15]
    return render(request, 'product/products.html', {
        'products': all_products,
    })


def products_red(request):
    url = reverse('home')
    return HttpResponseRedirect(url)


def product(request, ps):
    single_product = get_object_or_404(Product, slug=ps)
    all_products = Product.objects.filter(Q(title__contains=single_product.title) | Q(brand=single_product.brand) | Q(price__=single_product.price)).order_by("title")
    return render(request, "product/product.html", {
        'product': single_product,
        'products': all_products
    })


def contact(request):
    return render(request, 'product/Contact.html')


def site_header(request):
    return render(request, 'shared/site_header.html', )


def site_footer(request):
    return render(request, 'shared/site_footer.html', )
